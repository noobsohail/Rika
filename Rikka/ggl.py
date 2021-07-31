from telethon.tl.types import ChannelParticipantsAdmins
from telethon.utils import get_display_name
from telethon import *
from . import API_ID, API_HASH, BOT_TOKEN, tbot, OWNER
from Rikka.events import register
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import asyncio
import os
from shutil import rmtree
from .utils.google import googleimagesdownload

IN_GRP = -1001415010098
bot = asst = tbot
REQ_GO = -1001579439262
on = tbot.on
auth = OWNER

@tbot.on(events.NewMessage(chats=IN_GRP))
async def img(event):
    temxt = event.text
    if "/img" in temxt:
        sim = await event.pattern_match.group(1)
        if not sim:
            return await eod(event, "`Give something to search...`")
        hell = await eor(event, f"Searching for  `{sim}`...")
        if "-" in sim:
            try:
                lim = int(sim.split(";")[1])
                sim = sim.split(";")[0]
            except BaseExceptaion:
                lim = 5
        else:
            lim = 5
        imgs = googleimagesdownload()
        args = {
            "keywords": sim,
            "limit": lim,
            "format": "jpg",
            "output_directory": "./DOWNLOADS/",
        }
        letsgo = imgs.download(args)
        gotit = letsgo[0][sim]
        await event.client.send_file(event.chat_id, gotit, caption=sim, album=True)
        rmtree(f"./DOWNLOADS/{sim}/")
        await hell.delete()

"""
@tbot.on(events.NewMessage(chats=IN_GRP))
async def _(event):
    if event.fwd_from:
        return
    if "/rev" in event.text:
        start = datetime.datetime.now()
        BASE_URL = "http://www.google.com"
        OUTPUT_STR = "Reply to an image to do Google Reverse Search"
        if event.reply_to_msg_id:
            hell = await eor(event, "Pre Processing Media")
            previous_message = await event.get_reply_message()
            previous_message_text = previous_message.message
            if previous_message.media:
                downloaded_file_name = await bot.download_media(
                    previous_message, Config.TMP_DOWNLOAD_DIRECTORY
                )
                SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
                multipart = {
                    "encoded_image": (
                        downloaded_file_name,
                        open(downloaded_file_name, "rb"),
                    ),
                    "image_content": "",
                }
            # https://stackoverflow.com/a/28792943/4723940
                google_rs_response = requests.post(
                    SEARCH_URL, files=multipart, allow_redirects=False
                )
                the_location = google_rs_response.headers.get("Location")
                os.remove(downloaded_file_name)
            else:
                previous_message_text = previous_message.message
                SEARCH_URL = "{}/searchbyimage?image_url={}"
                request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
                google_rs_response = requests.get(request_url, allow_redirects=False)
                the_location = google_rs_response.headers.get("Location")
            await hell.edit("Found Google Result. Processing results...")
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
            }
            response = requests.get(the_location, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            # document.getElementsByClassName("r5a77d"): PRS
            prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
            prs_anchor_element = prs_div.find("a")
            prs_url = BASE_URL + prs_anchor_element.get("href")
            prs_text = prs_anchor_element.text
            # document.getElementById("jHnbRc")
            img_size_div = soup.find(id="jHnbRc")
            img_size = img_size_div.find_all("div")
            end = datetime.datetime.now()
            ms = (end - start).seconds
            OUTPUT_STR = """#Possible Related Search : <a href="{prs_url}">{prs_text}</a>
   # More Info: Open this <a href="{the_location}">Link</a> in {ms} seconds""".format(
     #           **locals()
     #       )
      #  await hell.edit(OUTPUT_STR, parse_mode="HTML", link_preview=False)
