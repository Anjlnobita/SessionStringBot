from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Start Generating Session", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Bot Status and More Bots", url="https://t.me/noxarion_network")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("More Amazing bots", url="https://t.me/noxarion_network")],
    ]

    START = """
**Hey {}

Welcome to {}

<blockquote>If you don't trust this bot, 
> Please stop reading this message
> Delete this chat</backquote>

Still reading?
You can use me to generate Pyrogram and Telethon string session. Use below buttons to learn more !

By @noxarion_network**
    """

    HELP = """
  **Available Commands**

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @noxarion_network


Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @meow_anjl
    """
