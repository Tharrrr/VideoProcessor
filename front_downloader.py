import sys
from pytubefix import YouTube
from pytubefix.cli import on_progress

urlf = sys.argv[1]
yt = YouTube(urlf, on_progress_callback=on_progress)
print(f"Downloading content video: {yt.title}")

ys = yt.streams.get_highest_resolution()
ys.download('downloads')
