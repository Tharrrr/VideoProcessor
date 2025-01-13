import subprocess
import re
import os

def split_video(input_video, output_pattern):
    # Run ffmpeg command to get the video duration
    result = subprocess.run(
        f"ffmpeg -i \"{input_video}\"", shell=True, capture_output=True, text=True, encoding='utf-8'
    )
    
    # Check if stderr contains data and extract the duration
    if result.stderr:
        duration_match = re.search(r'Duration: (\d+:\d{2}:\d{2}.\d{2})', result.stderr)
        if duration_match:
            # Extract and convert the duration to seconds
            duration_str = duration_match.group(1)
            hours, minutes, seconds = map(float, duration_str.split(":"))
            total_seconds = hours * 3600 + minutes * 60 + seconds
            
            # Split into 59-second clips, ensuring last clip is handled
            num_clips = int(total_seconds // 59) + 1  # Ensure to include the last partial clip
            for i in range(num_clips):
                start_time = i * 59
                output_file = output_pattern.format(i)
                # Ensure we don't exceed the total duration
                duration = 59 if start_time + 59 <= total_seconds else total_seconds - start_time
                
                # Re-encode the output clips to avoid codec-related issues
                subprocess.run(f"ffmpeg -i \"{input_video}\" -ss {start_time} -t {duration} "
                               f"-c:v libx264 -c:a aac -strict experimental \"{output_file}\"", shell=True)
        else:
            print(f"Error: Could not extract video duration from {input_video}.")
            print(f"ffmpeg stderr: {result.stderr}")
    else:
        print(f"Error: No stderr output for {input_video}.")
        print(f"ffmpeg stdout: {result.stdout}")

def list_and_select_video(folder_path):
    # List all .mp4 files in the folder
    video_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp4')]
    
    if not video_files:
        print("No .mp4 files found in the folder.")
        return None
    
    # Display the list of video files with index numbers
    print("Select a video file to process:")
    for index, video in enumerate(video_files):
        print(f"{index + 1}. {video}")
    
    # Ask the user to select a file by index
    try:
        selection = int(input(f"Enter the number (1-{len(video_files)}): "))
        if 1 <= selection <= len(video_files):
            selected_video = video_files[selection - 1]
            return os.path.join(folder_path, selected_video)
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def process_selected_video():
    downloads_folder = "downloads"  # Path to your "downloads" folder
    outputs_folder = "outputs"  # Path to the "outputs" folder

    # Create the 'outputs' folder if it doesn't exist
    if not os.path.exists(outputs_folder):
        os.makedirs(outputs_folder)

    selected_video = list_and_select_video(downloads_folder)
    
    if selected_video:
        # Generate the output pattern with formatting placeholder for each clip
        output_pattern = os.path.join(outputs_folder, f"{os.path.splitext(os.path.basename(selected_video))[0]}_clip_{{:03d}}.mp4")
        print(f"Processing {selected_video}...")
        split_video(selected_video, output_pattern)

# Example usage
process_selected_video()
