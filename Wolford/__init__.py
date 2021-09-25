import os
from pyrogram import Client
from telethon import TelegramClient


TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME")
DB_URL = os.environ.get("DB_URL")
SAUCE_API = os.environ.get("SAUCENAO_API")
ANILIST_CLIENT = os.environ.get("ANILIST_CLIENT")
ANILIST_SECRET = os.environ.get("ANILIST_SECRET")
ANILIST_REDIRECT_URL = os.environ.get("ANILIST_REDIRECT_URL", "https://anilist.co/api/v2/oauth/pin")
API_ID = int(os.environ.get("API_ID"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID"))
OWNER = list(filter(lambda x: x, map(int, os.environ.get("OWNER_ID").split())))  ## sudos can be included


#Requester.py
CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", "@AN1ME_HUB")
GROUP_USERNAME = os.environ.get("GROUP_USERNAME", "@AN1ME_HUB_DISCUSSION")
GROUP_ID = list(filter(lambda x: x, map(int, os.environ.get("GROUP_ID").split())))
REQ_CHANNEL_ID = os.environ.get("REQ_CHANNEL_ID", -1001176025751)
#BUTTONS IN REQUESTER
BTN1_NAME = os.environ.get("BTN1_NAME", "📜 Index 📜")
BTN1_LINK = os.environ.get("BTN1_LINK", "https://t.me/index_animehub")

BTN2_NAME = os.environ.get("BTN2_NAME", "Movies")
BTN2_LINK = os.environ.get("BTN2_LINK", "https://t.me/anime_hub_MOVIES")

BTN3_NAME = os.environ.get("BTN3_NAME", "Ongoing Anime")
BTN3_LINK = os.environ.get("BTN3_LINK", "https://t.me/Ongoing_Anime1")

DOWN_PATH = "Wolford/downloads/"
HELP_DICT = dict()

api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN

tbot = TelegramClient('anon', api_id, api_hash).start(bot_token=bot_token)

plugins = dict(root="Wolford/plugins")
Wolford = Client("Wolford", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=plugins)
