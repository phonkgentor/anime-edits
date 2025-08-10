from flask import Flask, request, render_template, send_from_directory
import os
from moviepy.editor import VideoFileClip

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
EDITED_FOLDER = 'edited'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EDITED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('video')
        if file and file.filename:
            upload_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(upload_path)

            edited_filename = f"edited_{file.filename}"
            edited_path = os.path.join(EDITED_FOLDER, edited_filename)

            clip = VideoFileClip(upload_path)
            duration = min(10, clip.duration)
            clip.subclip(0, duration).write_videofile(edited_path, audio_codec='aac', verbose=False, logger=None)
            clip.close()

            return render_template('index.html', edited_file=edited_filename)
    return render_template('index.html', edited_file=None)

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(EDITED_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
