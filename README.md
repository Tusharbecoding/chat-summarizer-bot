# 📝 Smart Conversation Summarizer Bot

A simple, powerful Discord bot that uses Google Gemini AI to summarize long conversations and provide daily digests for your server.

---

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Tusharbecoding/chat-summarizer-bot.git
   cd chat-summarizer-bot
   ```

---

## Features

- 🔍 **Flexible Summarization** – Summarize any number of messages from any channel
- ⚡ **Quick TLDR** – Instantly get a summary of the current conversation
- 📅 **Daily Digests** – 24-hour activity summaries for any channel

---

## Commands

| Command                       | Description                                          | Example                         |
| ----------------------------- | ---------------------------------------------------- | ------------------------------- |
| `!summarize #channel last 50` | Summarize last 50 messages from specified channel    | `!summarize #general last 100`  |
| `!tldr 15`                    | Quick summary of last 15 messages in current channel | `!tldr 25`                      |
| `!daily-summary #channel`     | 24-hour digest of channel activity                   | `!daily-summary #announcements` |

---

## Setup

1. **Discord Setup:**
   - Create a Discord bot and invite it to your server.
2. **Install Dependencies:**
   - Run: `pip install -r requirements.txt`
3. **Configure Environment:**
   - Create a `.env` file in the project root with your Discord and Gemini API tokens:
     ```env
     DISCORD_TOKEN=your_discord_token_here
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
4. **Run the Bot:**
   - Start the bot with: `python bot.py`

---

## Files

- `bot.py` – Main bot code
- `requirements.txt` – Python dependencies
- `.env` – Environment variables (tokens)

---

## Example Output

```
📝 Summary of #general
Last 25 messages

Main topics discussed:
- Project deadline discussion for Q4 launch
- New team member introductions
- Bug reports for login system

Key decisions:
- Moved deadline to December 15th
- John will handle the login bug fixes

Action items:
- Sarah to update project timeline
- Team meeting scheduled for Friday 2 PM
```

Perfect for busy Discord servers where you need to catch up quickly!
