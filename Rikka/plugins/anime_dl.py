import html
import bs4
import asyncio, requests, time, random
import re
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, Update
from .. import HELP_DICT, TRIGGERS as trg, BOT_NAME
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}


async def site_search(client: Client, message: Message, site: str):
    args = message.text.split(" ", 1)
    more_results = True

    try:
        search_query = args[1]
    except IndexError:
        await message.reply("Give something to search")
        return

    if site == "kaizoku":
        search_url = f"https://animekaizoku.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "post-title"})

        if search_result:
            result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKaizoku</code>: \n"
            for entry in search_result:
                post_link = "https://animekaizoku.com/" + entry.a['href']
                post_name = html.escape(entry.text)
                result += f"• <a href='{post_link}'>{post_name}</a>\n"
        else:
            more_results = False
            result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKaizoku</code>"

    elif site == "indi":
        search_url = f"https://indianime.com/?s={search_query}"
        html_text = requests.get(search_url, headers=headers).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h1", {"class": "elementor-post__title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>@IndiAnimein</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>@IndiAnimein</code>"
                more_results = False
                break

            post_link = entry.a["href"]
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"

    elif site == "ganime":
        search_url = f"https://gogoanime.so//search.html?keyword={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {"class": "title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>gogoanime</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>gogoanime</code>"
                more_results = False
                break

            post_link = entry.a["href"]
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"

   # buttons = InlineKeyboardMarkup([[InlineKeyboardButton("See All Results", url=search_url)]])

    if more_results:
        await message.reply(result + f"\n\n[More Results Here](search_url)", disable_web_page_preview=True)
    else:
        await message.reply(result)


@Client.on_message(filters.command(["kai", f"kai{BOT_NAME}"], prefixes=trg))
async def kaizoku(c: Client, update: Update):
    await site_search(c, update, "kaizoku")

@Client.on_message(filters.command(["indi", f"indi{BOT_NAME}"], prefixes=trg))
async def kyo(c: Client, update: Update):
    await site_search(c, update, "indi")

@Client.on_message(filters.command(["gogo", f"gogo{BOT_NAME}"], prefixes=trg))
async def gogo(c: Client, update: Update):
    await site_search(c, update, "ganime")

# HELP_DICT["anime_dl"] = ""
