import os
import json
from pyrogram import Client, filters

YOUTUBE = {
    "access_token": "your_access_token_here",
    "expires": 1730115155.251452,
    "refresh_token": "your_refresh_token_here",
    "token_type": "Bearer",
}


def generate_cookies():
    access_token = YOUTUBE["access_token"]
    os.system(
        f"yt-dlp --cookies cookies.txt --username oauth2 --password {access_token} --write-description --skip-download https://www.youtube.com/watch?v=LLF3GMfNEYU"
    )

@app.on_message(filters.command("cookies"))
async def send_cookies(client, message):
    try:
        generate_cookies()
        await message.reply_document("cookies.txt")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Welcome to the Cookies Generator Bot!")
