import asyncio
from pyrogram import Client, idle
from . import Wolford, tbot
from .utils.db import _close_db


async def main():
    await asyncio.gather(Wolford.start())
    await idle()
    await asyncio.gather(Wolford.stop())
    _close_db()

from Wolford import requester, ggl
print("Imported Requester, Google")

async def tmain():
    tbot.start()
    print("Bot Started")
    print("imported requester")

asyncio.get_event_loop().run_until_complete(main())
# tbot.run_until_disconnected(tmain())
