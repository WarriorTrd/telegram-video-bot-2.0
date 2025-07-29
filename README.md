# 📥 Vidzilla – Telegram All-in-One Media Downloader Bot

A Telegram bot built with Python and Docker that downloads media from popular platforms via [RapidAPI](https://rapidapi.com). Currently supports **Instagram**.

> ⚠️ This project is built to be easily extendable to support YouTube, TikTok, Twitter, and more. API limitations currently restrict functionality to Instagram only.

---

## 🚀 Features
- Download Instagram videos directly via Telegram
- Modular handler structure (easily extendable)
- Dockerized for clean deployment
- `.env` driven secrets management
- Stripe integration placeholder
- MongoDB for storing user data

---

## 🛠 Tech Stack
- Python 3.11
- Telegram Bot API
- RapidAPI
- Docker
- MongoDB

---

## 🔧 Setup Locally
```bash
# Clone and go into project
git clone https://github.com/yourusername/vidzilla.git
cd vidzilla

# Set up environment variables
cp .env.example .env

# Build Docker image
docker build -t vidzilla .

# Run container
docker run -d --env-file .env -p 8000:8000 vidzilla
