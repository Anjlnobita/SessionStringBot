import os
import json
from pyrogram import filters, Client as app 
from youtube_dl import YoutubeDL

YOUTUBE = {
    "access_token": "your_access_token_here",
    "expires": 1730115155.251452,
    "refresh_token": "your_refresh_token_here",
    "token_type": "Bearer",
}


async def check_auth_token():
    video_url = "https://www.youtube.com/watch?v=LLF3GMfNEYU"
    auth_token = os.getenv("TOKEN_DATA")
    opts = {
        "format": "bestaudio",
        "quiet": True,
        "username": "oauth2",
        "password": auth_token,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl.extract_info(video_url, download=False)
        return True
    except Exception:
        return False






@app.on_message(filters.command("authtoken") & filters.user(SUDOERS))
async def auth_token_status(client, message):
    status_message = "**Auth Token Status:**\nChecking..."
    status_msg = await message.reply_text(status_message)

    use_token = await check_auth_token()
    status_message = "**Auth Token Status:**\n"
    status_message += "✅ Alive" if use_token else "❌ Dead"
    await status_msg.edit_text(status_message)

    if not use_token:
        status_message += "\n\n**Generating a new Auth token...**"
        await status_msg.edit_text(status_message)
        try:
            os.system(
                f"yt-dlp --username oauth2 --password '' -F https://www.youtube.com/watch?v=LLF3GMfNEYU"
            )
            await message.reply_text("**✅ Successfully generated a new token.**")
        except Exception as ex:
            await message.reply_text(
                f"**❌ Failed to generate a new token: {str(ex)}**"
            )

def generate_cookies():
    access_token = YOUTUBE["access_token"]
    refresh_token = YOUTUBE["refresh_token"]
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
