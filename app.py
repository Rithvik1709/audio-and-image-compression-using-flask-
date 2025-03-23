from flask import Flask, request, render_template, send_from_directory
import os
from PIL import Image
import wave

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
COMPRESSED_FOLDER = 'compressed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['COMPRESSED_FOLDER'] = COMPRESSED_FOLDER

# Home Page
@app.route('/')
def upload_file():
    return render_template('index.html')

# Handle File Upload and Compression
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    compression_percentage = int(request.form.get('compression_percentage', 50))  # Default to 50%

    if file.filename == '':
        return "No selected file", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    file_ext = file.filename.split('.')[-1].lower()

    if file_ext in ['jpg', 'jpeg', 'png']:
        compressed_path = compress_image(filepath, compression_percentage)
    elif file_ext in ['wav']:
        compressed_path = compress_audio(filepath, compression_percentage)
    else:
        return "Unsupported file type", 400

    return f"File compressed successfully. <a href='/download/{os.path.basename(compressed_path)}'>Download</a>"
def compress_image(filepath, compression_percentage):
    img = Image.open(filepath)

    # Resize image based on compression percentage
    width, height = img.size
    scale_factor = 1 - (compression_percentage / 100)
    new_width = max(50, int(width * scale_factor))  # Prevent too small images
    new_height = max(50, int(height * scale_factor))
    
    img = img.resize((new_width, new_height), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS

    compressed_path = os.path.join(app.config['COMPRESSED_FOLDER'], "compressed_" + os.path.basename(filepath))
    
    # Reduce quality for JPG, use PNG compression for PNG
    if filepath.endswith('.png'):
        img.save(compressed_path, optimize=True, quality=20)
    else:
        img.save(compressed_path, quality=max(10, 100 - compression_percentage), optimize=True)
    
    return compressed_path


# Audio Compression (Adjust sample rate based on percentage)
def compress_audio(filepath, compression_percentage):
    with wave.open(filepath, 'rb') as audio:
        params = list(audio.getparams())
        sample_rate = params[2] * (1 - (compression_percentage / 100))
        params[2] = max(8000, int(sample_rate))  # Ensure minimum sample rate of 8kHz
        
        compressed_path = os.path.join(app.config['COMPRESSED_FOLDER'], "compressed_" + os.path.basename(filepath))
        
        with wave.open(compressed_path, 'wb') as new_audio:
            new_audio.setparams(tuple(params))
            new_audio.writeframes(audio.readframes(audio.getnframes()))
    
    return compressed_path

# Download Compressed File
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['COMPRESSED_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
