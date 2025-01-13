# Video Processing Automation Scripts

This project provides a set of Python scripts that automate the process of downloading, splitting, and combining YouTube videos for creating short-form content. It uses a combination of libraries such as `pytubefix` for downloading videos and `moviepy` for video editing.

## Features
1. **Background Video Download**: Downloads a background video from YouTube.
2. **Content Video Download**: Downloads a content video from YouTube.
3. **Splitting Videos into Clips**: Splits the content video into 59-second clips using `ffmpeg`.
4. **Joining Clips**: Combines clips into a final video with a split-screen effect.

## Requirements

Make sure you have the following dependencies installed:

- `pytubefix`: To download YouTube videos.
- `moviepy`: To edit and manipulate video files.
- `ffmpeg-python`: To run `ffmpeg` commands from Python for video processing.

You can install all dependencies using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
