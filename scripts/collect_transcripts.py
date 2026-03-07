from utils.youtube_metadata_loader import fetch_video_data

videos = [
    "dQw4w9WgXcQ",
    "9bZkp7q19f0"
]

for vid in videos:

    print("Downloading:", vid)

    fetch_video_data(vid)

print("All transcripts saved")