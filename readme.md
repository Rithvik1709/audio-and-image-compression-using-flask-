# Audio and Image Compression using Flask

## Overview
This project is a Flask-based web application that enables users to upload audio and image files for compression. It utilizes efficient compression algorithms to reduce file sizes while maintaining quality.

## Features
- Upload and compress image files (JPEG, PNG, etc.)
- Upload and compress audio files (MP3, WAV, etc.)
- Display/download the compressed files
- Simple and user-friendly web interface

## Technologies Used
- Python
- Flask (for backend API and web handling)
- PIL (for image processing)
- FFmpeg  (for audio processing)
- HTML (for frontend)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip

### Steps to Set Up
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/audio-image-compression.git
   cd audio-image-compression
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```


## Folder Structure
```
project-root/            
│── templates/           # HTML Templates
│── uploads/             # Uploaded files
│── compressed/          # Compressed files
│── app.py               # Flask app
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```
