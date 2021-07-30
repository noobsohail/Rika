import asyncio
from pyrogram import Client, idle
from . import Rika, tbot
from .utils.db import _close_db


async def main():
    await asyncio.gather(Rika.start())
    await idle()
    await asyncio.gather(Rika.stop())
    _close_db()

from Rika import requester, ggl
print("Imported Requester, Google")

async def tmain():
    tbot.start()
    print("Bot Started")
    print("imported requester")

asyncio.get_event_loop().run_until_complete(main())
# tbot.run_until_disconnected(tmain())
