import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from .. import HELP_DICT, TRIGGERS as trg, BOT_NAME , HELP_DICT

@run_async
def paste(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text

    elif len(args) >= 1:
        data = message.text.split(None, 1)[1]

    else:
        message.reply_text("What am I supposed to do with this?")
        return

    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": data})
        .json()
        .get("result")
        .get("key")
    )

    url = f"https://nekobin.com/{key}"

    reply_text = f"Nekofied to *Nekobin* : {url}"

    message.reply_text(
        reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
    )

HELP_DICT["Paste"] = """ *Usage
/paste - To paste text or code in nekobin.com
"""