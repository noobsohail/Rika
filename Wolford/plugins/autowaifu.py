import requests
from asyncio import sleep
from bs4 import BeautifulSoup as bs
from pyrogram import *
from pyrogram.types import Message
import time
import os
from Wolford import *

xyz = "A qt waifu appeared! Add them to your harem by sending /protecc character name"

@Client.on_message(filters.command(['wai', f'wai{BOT_NAME}'], prefixes=TRIGGERS))
async def saucenao(client: Client, message: Message):
    reply = message.reply_to_message
    media = reply.photo
    if not media:
        await message.reply_text('Bhag Bsdk')
        return
    dl = await client.download_media(media, "resources/")
    file = {"encoded_image": (dl, open(dl, "rb"))}
    grs = requests.post(
        "https://www.google.com/searchbyimage/upload",
        files=file,
        allow_redirects=False,
    )
    loc = grs.headers.get("Location")
    response = requests.get(
        loc,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        },
    )
    xx = bs(response.text, "html.parser")
    div = xx.find_all("div", {"class": "r5a77d"})[0]
    alls = div.find("a")
    text = alls.text
    await client.send_message(message.chat.id, f"**query:** `{text}` ")
    await sleep(5)
    os.remove(dl)
