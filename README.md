 Anime Highlight Generator
![Anime Highlight Generator](https://i.imgur.com/9wUoFSe.png)
A professional-grade tool that automatically creates stunning anime highlight videos with synchronized phonk music. Perfect for creating viral social media edits in both YouTube (16:9) and Instagram (9:16) formats.
## ✨ Features
- **Advanced Scene Detection**: Automatically identifies the most intense action scenes in any anime video
- **Professional Effects**: Cinematic color grading, dynamic glitches, zoom pulses, and flash effects
- **Music Synchronization**: Perfectly timed visual effects that match the beats of phonk music
- **Dual Format Output**: Creates both landscape (YouTube) and portrait (Instagram) versions
- **High Quality**: Outputs high bitrate H.264 video with AAC audio for maximum compatibility
## 🚀 Quick Start
### Option 1: Use the Web Version
Visit our [website](https://phonkgentor.github.io/anime-highlight-generator) to use the online version of the tool.
### Option 2: Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/phonkgentor/anime-highlight-generator.git
   cd anime-highlight-generator
Install dependencies:

pip install -r requirements.txt
Run the application:

python main.py
Open your browser and go to: http://localhost:5000

📋 Requirements
Python 3.8 or higher
FFmpeg installed on your system
4GB RAM minimum (8GB recommended for HD videos)
🛠️ Command Line Usage
You can also use the tool directly from the command line:

python video_processor.py /path/to/anime_video.mp4
This will automatically:

Detect the most action-packed scenes
Download phonk music
Create highlight edits in both YouTube and Instagram formats
Save the results to the output directory
⚙️ Configuration
You can customize the tool by editing config.json:

{
  "youtube_format": {
    "width": 1280,
    "height": 720,
    "duration": 180
  },
  "instagram_format": {
    "width": 720,
    "height": 1280,
    "duration": 60
  },
  "effect_intensity": 0.8,
  "phonk_type": "drift"
}
📚 How It Works
Scene Detection: The tool analyzes video frame differences to identify scenes with the most motion and activity
Audio Analysis: Phonk music is downloaded and analyzed for beat patterns
Effect Generation: Visual effects are applied and synchronized with the music beats
Format Adaptation: Videos are converted to both landscape and portrait orientations
📱 Mobile Support
The web version works on mobile devices, allowing you to:

Upload videos from your phone's gallery
Preview the results directly on your device
Download the edited videos to share on social media
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements
FFmpeg for video processing capabilities
yt-dlp for phonk music download functionality
All the amazing anime creators whose content inspires us
Made with ❤️ by anime fans, for anime fans.

Website |
GitHub |
Report Issues

## Step 5: Create assets folder structure (Optional but recommended)
For the gallery to work properly, you'll need to create these folders:
- `assets/thumbs/`
- `assets/videos/`
## How to Deploy to GitHub Pages
1. Create a GitHub account with username "phonkgentor" if you haven't already
2. Go to GitHub.com and log in
3. Click the "+" icon in the top right corner and select "New repository"
4. Set the repository name to "anime-highlight-generator"
5. Leave it as Public
6. Click "Create repository"
7. You'll see a page with setup instructions. Click on "uploading an existing file"
8. Upload all the files you created above (index.html, gallery.html, styles.css, README.md)
9. Add a commit message like "Initial website files" and click "Commit changes"
10. Go to the repository Settings tab
11. In the left sidebar, click on "Pages"
12. Under "Source", select "main" from the dropdown
13. Click "Save"
14. Wait a few minutes for GitHub to build your site
15. Your site will be available at https://phonkgentor.github.io/anime-highlight-generator/
