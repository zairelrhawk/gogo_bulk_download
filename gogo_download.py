import time
import requests

# Function to check if URL is valid
def is_valid_url(url):
    if len(url) < 3:
        return False
    return True

# Function to download episode
def download_episode(url, episode_number, video_quality, download_path):
    print(f"Downloading episode {episode_number}...")
    time.sleep(2)  # Simulating download time

    # Replace this with your actual download logic
    print("Waiting for 10 seconds...")
    time.sleep(10)
    # Here, we are just printing the download details
    print(f"Episode {episode_number} downloaded in {video_quality} quality.")

# Main function
def main():
    # Get user inputs
    episode_1_url = input("Enter the episode 1 URL: ")
    start_episode = int(input("From which episode do you want to download? (Enter episode number): "))
    end_episode = int(input("To which episode do you want to download? (Enter episode number): "))
    video_quality = int(input("Enter the video quality you want to download (1 for 360p, 2 for 480p, 3 for 720p, 4 for 1080p): "))
    action = int(input("Enter 1 to download episodes or 2 to save episode links to a text file: "))
    output_file_name = input("Enter the output file name: ")
    download_path = input("Enter the storage path where the download files will be saved: ")

    # Check if the URL is valid
    if not is_valid_url(episode_1_url):
        print("Invalid URL. Exiting...")
        return

    # Check if the start episode is valid
    if start_episode == 0:
        print("Start episode cannot be 0. Exiting...")
        return

    # If end episode is the same as start episode, download only that episode
    if start_episode == end_episode:
        episodes_to_download = [start_episode]
    else:
        episodes_to_download = list(range(start_episode, end_episode + 1))

    # Perform the selected action
    if action == 1:
        print("THE REQUIRED EPISODES ARE NOW BEEN DOWNLOADING")
        for episode in episodes_to_download:
            episode_url = episode_1_url + str(episode)
            download_episode(episode_url, episode, video_quality, download_path)
            print(f"Episode {episode} downloaded.")
        print("DONE")
    elif action == 2:
        with open(output_file_name, "w") as file:
            for episode in episodes_to_download:
                episode_url = episode_1_url + str(episode)
                file.write(f"Episode {episode}: {episode_url}\n")
        print("Episode links saved to file.")
    else:
        print("Invalid action. Exiting...")

# Run the main function
if __name__ == "__main__":
    main()
