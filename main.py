import subprocess

def run_script(script_name, url=None):
    """Run the script with the URL passed as an argument, if provided."""
    try:
        # Build the command
        command = ['python', script_name]
        if url:
            command.append(url)

        # Run the script
        subprocess.run(command, check=True)
        print(f"{script_name} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing {script_name}: {e}")

def main():
    # Step 1: Background video download
    print("Background video download")
    if input("Do you want to download the background video? (yes/no): ").strip().lower() == 'yes':
        url = input('Enter the background URL: ')
        run_script('background_download.py', url)
    else:
        print("Skipping background video download.")

    # Step 2: Content video download
    print("\nContent video download")
    if input("Do you want to download the content video? (yes/no): ").strip().lower() == 'yes':
        urlf = input('Enter the content URL: ')
        run_script('front_download.py', urlf)
    else:
        print("Skipping content video download.")

    # Step 3: Split video into clips
    print("\nSplitting video into clips")
    if input("Do you want to split the content video into clips? (yes/no): ").strip().lower() == 'yes':
        run_script('split.py')  # No URL needed for split.py
    else:
        print("Skipping video splitting.")

    # Step 4: Join clips into the final video
    print("\nJoining clips into the final video")
    if input("Do you want to join the clips into the final video? (yes/no): ").strip().lower() == 'yes':
        run_script('joiner.py')  # No URL needed for joiner.py
    else:
        print("Skipping video joining.")

if __name__ == "__main__":
    main()
