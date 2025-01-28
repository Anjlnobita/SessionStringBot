import os
import json
from pyrogram import filters, Client as app 
from yt_dlp import YoutubeDL


YOUTUBE = {
    "access_token": "ya29.a0AeDClZCF9VQ_t37HaJoqexLY961mvpqTM1rqdvDbLvMEmOnFAUKtQ_4GModmKm4bLHL5vJj5Wuv3WfGXC1GPsrA9K-f0biQszZTy7a3JbwMgaWRF9Cepk8YcfgVB9Ase0gQHArF267CrKZwcDiXX2IInJSYMM5sNp5wUP1JI3XWcM-DZBMnRaCgYKAbYSARISFQHGX2MihJR7K7A7JLDmzn4yRmtwDQ0187",
    "expires": 1730115155.251452,
    "refresh_token": "1//056BOYS8QzxrYCgYIARAAGAUSNwF-L9Irwl_Edq4pOz6ylq9vxSqXAyaPMSc9k4IV4sKOy66xHLbuG--4Hx3rp9r29voH71M7eFk",
    "token_type": "Bearer",
}


def nobii():
    TOKEN_DATA = os.getenv("TOKEN_DATA")
    if not TOKEN_DATA:
        os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)






async def check_cookies(video_url):
    cookie_file = get_random_cookie()
    opts = {
        "format": "bestaudio",
        "quiet": True,
        "cookiefile": cookie_file,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl.extract_info(video_url, download=False)
        return True
    except:
        return False


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
    except:
        return False


@app.on_message(filters.command("noiii"))
async def cookies_status(client, message):
    status_message = "**Cookie Status:**\nChecking..."
    status_msg = await message.reply_text(status_message)

    cookie_status = await check_cookies("https://www.youtube.com/watch?v=LLF3GMfNEYU")
    status_message = "**Cookie Status:**\n"
    status_message += "✅ Alive" if cookie_status else "❌ Dead"
    await status_msg.edit_text(status_message)


@app.on_message(filters.command("authtoken"))
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

