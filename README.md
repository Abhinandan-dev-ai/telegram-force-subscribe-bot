# 🤖 Telegram Force-Subscribe Bot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-2CA5E0?logo=telegram&logoColor=white)](https://core.telegram.org/bots)
[![Stars](https://img.shields.io/github/stars/Abhinandan-dev-ai/telegram-force-subscribe-bot?style=social)](https://github.com/Abhinandan-dev-ai/telegram-force-subscribe-bot/stargazers)
[![Forks](https://img.shields.io/github/forks/Abhinandan-dev-ai/telegram-force-subscribe-bot?style=social)](https://github.com/Abhinandan-dev-ai/telegram-force-subscribe-bot/network/members)

A lightweight, easy-to-deploy Telegram bot that requires users to join your channel or group before they can interact with it. Includes bilingual (English + Hindi) funny nudge messages to encourage joining!

---

## ✨ Features

- 🔒 **Force-subscribe gate** — non-members cannot use the bot until they join
- 😄 **Bilingual funny messages** — unique Hindi & English messages rotate per user so they never repeat back-to-back
- 📊 **Progress bar UI** — visual nudge showing 0% progress until they join
- ℹ️ **"Why Join?" button** — inline explanation to convince hesitant users
- ⚙️ **Environment-variable config** — no hardcoded secrets, safe to open-source
- 🪵 **Built-in logging** — easy debugging with timestamped logs

---

## 📋 Prerequisites

- Python 3.10 or higher
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- A public Telegram channel or group

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Abhinandan-dev-ai/telegram-force-subscribe-bot.git
cd telegram-force-subscribe-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your values:

```env
BOT_TOKEN=123456789:ABCDefgh...
CHANNEL_USERNAME=mychannel
```

### 4. Run the bot

```bash
python bot.py
```

---

## 🗂️ Project Structure

```
telegram-force-subscribe-bot/
├── bot.py            # Main bot logic
├── .env.example      # Template for environment variables
├── .env              # Your actual secrets (never commit this!)
├── requirements.txt  # Python dependencies
├── LICENSE           # MIT License
└── README.md         # This file
```

---

## ⚙️ Configuration

| Variable | Description | Example |
|----------|-------------|---------|
| `BOT_TOKEN` | Your bot's API token from BotFather | `123:ABCxyz...` |
| `CHANNEL_USERNAME` | Channel username **without** `@` | `mychannel` |

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgements

Built with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

---

<p align="center">
  <sub>Made with ❤️ by <a href="https://github.com/Abhinandan-dev-ai"><b>Abhinandan</b></a></sub>
</p>
