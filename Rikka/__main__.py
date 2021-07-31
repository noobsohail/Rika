import asyncio
from pyrogram import Client, idle
from . import Rikka, tbot
from .utils.db import _close_db


async def main():
    await asyncio.gather(Rikka.start())
    await idle()
    await asyncio.gather(Rikka.stop())
    _close_db()

from Rikka import requester, ggl
print("Imported Requester, Google")

async def tmain():
    tbot.start()
    print("Bot Started")
    print("imported requester")

asyncio.get_event_loop().run_until_complete(main())
# tbot.run_until_disconnected(tmain())
