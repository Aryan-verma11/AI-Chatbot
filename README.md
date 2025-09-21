# AI-Chatbot
An AI-powered chatbot that automates real-time conversations using Google Gemini API. It reads chat history, detects the latest sender, and replies in short Hinglish messages like a human. Built with Python, PyAutoGUI, and Pyperclip for automation.

✨ Features

📝 Reads and analyzes chat history automatically

🤝 Detects last sender before replying

🗣️ Replies in short Hinglish (no emojis, no punctuation like ? ! " ')

⚡ Uses Google Gemini AI for natural responses

⌨️ Automates copy-paste and message sending with PyAutoGUI

📋 Clipboard handling via Pyperclip

🛠️ Tech Stack

Python

PyAutoGUI
 – UI automation

Pyperclip
 – Clipboard handling

Google Generative AI (Gemini)
 – AI responses

🚀 How It Works

The script selects and copies chat history.

AI checks if the last message is from a specific sender.

If yes, Gemini generates a Hinglish reply.

The bot pastes and sends the reply automatically.