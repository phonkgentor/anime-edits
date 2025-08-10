# Anime Auto Editor

This project provides a simple web interface that automatically trims uploaded anime or video files to the first 10 seconds and offers the result for download.

## Features
- Upload any video file through the browser
- Server automatically shortens the video to 10 seconds
- Download the edited video

## Getting Started
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application
   ```bash
   python app.py
   ```
3. Open a browser and go to [http://localhost:5000](http://localhost:5000)
4. Upload a video and download the edited result

## Requirements
- Python 3.8+
- FFmpeg (for moviepy to process videos)

## License
MIT
