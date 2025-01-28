import uvloop

uvloop.install()
import asyncio  

from pyropatch import pyropatch 
from pyrogram import Client, idle, __version__  
from pyrogram.raw.all import layer 
from ssnbot import APP_ID, API_HASH, BOT_TOKEN, LOGGER  


async def main():
    plugins = dict(root="ssnbot/plugins")
    app = Client(
        name="ssnbot",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=plugins,
    )
    async with app:
        me = app.me
        LOGGER.info(
            "%s - @%s - Pyrogram v%s (Layer %s) - Started...",
            me.first_name,
            me.username,
            __version__,
            layer,
        )
        await idle()
        LOGGER.info("%s - @%s - Stopped !!!", me.first_name, me.username)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
