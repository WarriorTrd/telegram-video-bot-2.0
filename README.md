

# 🎥 Telegram Video Bot 2.0 – Lightweight Instagram Downloader

A minimal, Telegram-based media downloader bot built in Python with Docker support. While originally intended to support multiple platforms like YouTube, TikTok, and Twitter, the current free-tier API only supports **Instagram**.

> 🛠 Still a work in progress. Supports Instagram video download. Built with future expansion in mind.

---

## 🔑 Key Features

- 📥 Download Instagram videos directly via Telegram
- 📁 Automatically cleans up temporary files after download
- 🧩 Modular project structure for scalability
- 🌐 Multilingual support (EN, RU, UA — Uzbek coming soon)
- 🐳 Dockerized for easy deployment anywhere
- 🔐 Uses `.env` for safe API key and token management
- 📊 MongoDB integration for user/session management

---

## 🧠 Stack & Tools Used

- Python 3.11
- [Aiogram](https://github.com/aiogram/aiogram) (Telegram bot framework)
- Docker
- MongoDB
- RapidAPI (All-in-One Downloader)

---

## 🚀 Get Started

```bash
# Clone the repo
git clone https://github.com/WarriorTrd/telegram-video-bot-2.0.git
cd telegram-video-bot-2.0

# Set up environment
cp .env.example .env
# (Fill in your TELEGRAM bot token and RapidAPI key)

# Build Docker image
docker build -t telegram-bot .

# Run the bot
docker run -d --env-file .env -p 8000:8000 telegram-bot
````

---

## 🗂️ Project Structure

```
.
├── handlers/           # Bot command handlers
├── scripts/            # Auxiliary scripts (e.g. file handling)
├── utils/              # Utility functions (e.g. DB, logging)
├── wiki/               # Optional documentation
├── tests/              # Unit tests (in progress)
├── .env.example        # Template for secrets
├── Dockerfile          # Docker configuration
└── bot.py              # Main bot entrypoint
```

---

## 📌 Notes

* This bot currently works **only with Instagram** due to API limitations.
* Future updates may include:

  * Full multilingual interface (including Uzbek 🇺🇿)
  * YouTube/TikTok support (once proper API access is secured)
  * Persistent user sessions via MongoDB

---

## 🧑‍💻 Author

Built by [@WarriorTrd](https://github.com/WarriorTrd) during a summer side project.
Feel free to fork, suggest improvements, or contribute to multilingual support.

---

## 🪪 License

MIT License. Feel free to use, adapt, and deploy — but give credit if you're feeling kind.

```

---

## 🟢 What This Does:
- Removes obvious copy-paste vibes.
- Emphasizes **your** voice, intentions, and current limitations.
- Makes it resume/portfolio ready.
- Mentions future plans (Uzbek, multi-platform support).

---

Would you like a **Uzbek translation** section or a badge on top like `![Status: Beta]` or `Made with ❤️ in Uzbekistan`?

Let me know and I’ll add that too.
```

