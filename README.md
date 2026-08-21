# OneFileTelegramBot

A lightweight single-file Telegram bot that sends a file to all users.
Admins can update the file and broadcast messages directly via the admin panel.

## Features

- Broadcast a file to all registered users
- Update the file and messages without restarting
- Built-in admin panel for management
- Simple middleware and FSM state handling

## Requirements

- Python 3.12+

## Quick Start

**1. Clone the repository**

git clone https://github.com/SaySoGooD/OneFileTelegramBot.git
cd OneFileTelegramBot

**2. Create and activate a virtual environment**

python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

**3. Install dependencies**

pip install -r requirements.txt

**4. Configure**

Open config.py and set your values:
- TOKEN_BOT — your bot token from @BotFather
- ADMINS — list of admin Telegram IDs

**5. Run**

python main.py

## License

MIT
