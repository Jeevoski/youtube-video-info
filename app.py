from flask import Flask, render_template, request
from googleapiclient.discovery import build
import re

app = Flask(__name__)

API_KEY = "api_key"

def extract_video_id(url):
    pattern = r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|shorts/|v/))([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None

# ... keep the imports and other code unchanged ...

@app.route("/", methods=["GET", "POST"])
def index():
    video = {}
    error = ""

    if request.method == "POST":
        url = request.form.get("video_url", "").strip()
        vid = extract_video_id(url)

        if not vid:
            error = "Invalid YouTube URL."
        else:
            try:
                youtube = build("youtube", "v3", developerKey=API_KEY)
                response = youtube.videos().list(
                    part="snippet,statistics",
                    id=vid
                ).execute()

                if not response["items"]:
                    error = "Video not found."
                else:
                    item = response["items"][0]
                    video = {
                        "video_id": vid,                              # ← ADD THIS
                        "title": item["snippet"]["title"],
                        "channel": item["snippet"]["channelTitle"],
                        "description": item["snippet"]["description"],
                        "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
                        "views": item["statistics"].get("viewCount", "N/A")
                    }

            except Exception as e:
                error = str(e)

    return render_template("index.html", video=video, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5500)
