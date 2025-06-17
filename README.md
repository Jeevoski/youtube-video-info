# youtube-video-info
A sleek Flask web app to fetch YouTube video details like title, views, thumbnail, and description using the YouTube Data API. Includes related video suggestions and external download support via y2mate. Responsive UI with dark mode toggle. Ideal for learning API integration and Flask basics.
# 🎬 YouTube Video Info Fetcher

A clean and responsive Flask web app that fetches and displays details of any public YouTube video using the YouTube Data API. It also shows related videos and provides safe external download options via y2mate.

---

## 🚀 Features

- 🎥 Fetch video title, channel, views, and description  
- 🖼️ Show thumbnail preview  
- 🔗 Watch on YouTube button  
- 📥 External download via y2mate  
- 🔁 Related video suggestions  
- 🌗 Light/Dark mode toggle  
- ✅ Mobile responsive design  
- 🧠 Suggestions for better use

---

## 📸 Demo

![screenshot](screenshot.png)

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask**
- **Jinja2**
- **YouTube Data API v3**
- **Bootstrap 5**
- **HTML/CSS/JS**
- **Google Fonts**

---

## 📝 Prerequisites

- Python 3.x installed
- pip installed
- A Google Cloud project with the **YouTube Data API v3** enabled
- A valid **YouTube Data API Key**

---

## 🔑 How to Get an API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Go to **APIs & Services > Library**
4. Enable **YouTube Data API v3**
5. Go to **APIs & Services > Credentials**
6. Click **Create Credentials > API key**
7. Copy the key and paste it in `app.py`

---

## 🖥️ Local Setup

`bash
# 1. Clone the repository
git clone https://github.com/your-username/youtube-info-fetcher.git
cd youtube-info-fetcher

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key
# Open app.py and replace YOUR_API_KEY with your actual key

# 5. Run the app
python app.py

structure
├── templates/
│   └── index.html
├── static/ (optional if you add CSS/JS)
├── app.py
├── requirements.txt
└── README.md
