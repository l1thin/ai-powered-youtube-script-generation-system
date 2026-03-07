from utils.youtube_loader import fetch_transcript

videos = [
    "dQw4w9WgXcQ",
    "9bZkp7q19f0"
]

for vid in videos:
    print("Downloading:", vid)
    fetch_transcript(vid)

print("All transcripts saved")