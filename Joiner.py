import os
from moviepy.editor import *
from moviepy.video.fx.all import crop

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the input directories relative to the script's directory
outputs_dir = os.path.join(script_dir, "outputs")
background_dir = os.path.join(script_dir, "background")
output_dir = os.path.join(script_dir, "shorts")

# Ensure the directories exist
if not os.path.exists(outputs_dir):
    print(f"Error: The 'outputs' folder does not exist at {outputs_dir}")
    exit()
if not os.path.exists(background_dir):
    print(f"Error: The 'background' folder does not exist at {background_dir}")
    exit()

# List files in the outputs and background directories
outputs_files = os.listdir(outputs_dir)
background_files = os.listdir(background_dir)

# Show the available files and get user selection
print("Available videos in 'outputs' folder:")
for i, file in enumerate(outputs_files, 1):
    print(f"{i}. {file}")

video1_choice = int(input("Choose the video from 'outputs' (enter number): ")) - 1
video1_path = os.path.join(outputs_dir, outputs_files[video1_choice])

print("\nAvailable videos in 'background' folder:")
for i, file in enumerate(background_files, 1):
    print(f"{i}. {file}")

video2_choice = int(input("Choose the video from 'background' (enter number): ")) - 1
video2_path = os.path.join(background_dir, background_files[video2_choice])

# Load the chosen videos
video1 = VideoFileClip(video1_path)
video2 = VideoFileClip(video2_path)

# Crop and resize video 1
(w, h) = video1.size
if w > h:
    # The video is landscape
    crop_size = h
    x1, y1 = (w - crop_size) // 2, 0
else:
    # The video is portrait or square
    crop_size = w
    x1, y1 = 0, (h - crop_size) // 2
x2, y2 = x1 + crop_size, y1 + crop_size
bg_video = crop(video1, width=crop_size, height=crop_size, x_center=w/2, y_center=h/2)
bg_video = bg_video.resize((1080, 960))

# Crop and resize video 2
(w, h) = video2.size
if w > h:
    # The video is landscape
    crop_size = h
    x1, y1 = (w - crop_size) // 2, 0
else:
    # The video is portrait or square
    crop_size = w
    x1, y1 = 0, (h - crop_size) // 2
x2, y2 = x1 + crop_size, y1 + crop_size
bg_video2 = crop(video2, width=crop_size, height=crop_size, x1=x1, y1=y1, x2=x2, y2=y2)
bg_video2 = bg_video2.resize((1080, 960))
bg_video2 = bg_video2.set_duration(bg_video.duration)

# Set the position of the videos in the final video
video1_pos = (0, 0)
video2_pos = (0, 960)

# Create the final video by concatenating the two videos
final_video = CompositeVideoClip([bg_video.set_pos(video1_pos), 
                                  bg_video2.set_pos(video2_pos)], 
                                  size=(1080, 1920))

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define the output path and write the final video to disk
output_path = os.path.join(output_dir,'final-video.mp4')
final_video.write_videofile(output_path, fps=30)
