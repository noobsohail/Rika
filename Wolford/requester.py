from telethon.tl.types import ChannelParticipantsAdmins
from telethon.utils import get_display_name
from telethon import *
from Wolford import *
from Wolford.events import register
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

IN_GRP = GROUP_ID
bot = asst = tbot
REQ_GO = REQ_CHANNEL_ID
on = tbot.on
auth = OWNER


@tbot.on(events.NewMessage(chats=IN_GRP))
async def filter_requests(event):
    if event.fwd_from:
        return
    if "#request" in event.text:
      #  await asst.send_message(IN_GRP,
        #                    f"**We are not taking any requests for some days.\n\nSorry for inconvenience 😶**",
        #                    buttons=[
        #                        [Button.url("💠 Channel 💠", url=f"https://t.me/{CHANNEL_USERNAME}"),
        #                        Button.url("⚜️ Group ⚜️", url=f"https://t.me/{GROUP_USERNAME}")],
        #                        [Button.url("📜 Index 📜", url="https://t.me/index_animehub"),
        #                        Button.url("🎬 Movies 🎬", url=f"https://t.me/{CHANNEL_USERNAME}_MOVIES")],
        #                        [Button.url("💌 AMV 💌", url="https://t.me/AnimeHub_Amv")]])
        if (event.reply_to_msg_id):
            msg = (await event.get_reply_message()).message
        else:
            msg = event.text
        try:
            global user
            sender = event.sender
            if sender.bot:
                return
            if not sender.username:
                user = f"[{get_display_name(sender)}](tg://user?id={event.sender_id})"
            else:
                user = "@" + str(sender.username)
        except BaseException:
            user = f"[User](tg://user?id={event.sender_id})"
        chat_id = (str(event.chat_id)).replace("-100", "")
        username = ((await bot.get_entity(REQ_GO)).username)
        hel_ = "#request"
        if hel_ in msg:
            global anim
            anim = msg.replace(hel_, "")
        x = await asst.send_message(REQ_GO,
                                f"**Request By {user}**\n\n{msg}",
                                buttons=[
                                    [Button.url("Requested Message", url=f"https://t.me/c/{chat_id}/{event.message.id}")],
                                    [Button.inline("🚫 Reject", data="reqdelete"),
                                    Button.inline("Done ✅", data="isdone")],
                                    [Button.inline("⚠️ Unavailable ⚠️", data="unavl")]])
        btns = [
            [Button.url("⏳ Request Status ⏳", url=f"https://t.me/{username}/{x.id}")],
            [Button.url("💠 Channel 💠", url=f"https://t.me/{CHANNEL_USERNAME}"),
            Button.url("⚜️ Group ⚜️", url=f"https://t.me/{GROUP_USERNAME}")],
            [Button.url(f'{BTN1_NAME}', url=f'{BTN1_LINK}'),
            Button.url(f'{BTN2_NAME}', url=f'{BTN2_LINK}')],
            [Button.url(f'{BTN3_NAME}', url=f'{BTN3_LINK}')]]
        await event.reply(f"**👋 Hello {user} !!**\n\n📍 Your Request for  `{anim}`  has been submitted to the admins.\n\n🚀 Your Request Will Be Uploaded In 48hours or less.\n📌 Please Note that Admins might be busy. So, this may take more time. \n\n**👇 See Your Request Status Here 👇**", buttons=btns)
        if not auth:
            async for x in bot.iter_participants(f'@{GROUP_USERNAME}', filter=ChannelParticipantsAdmins):
                auth.append(x.id)

@tbot.on(events.callbackquery.CallbackQuery(data="reqdelete"))
async def delete_message(event):
    if not auth:
        async for x in bot.iter_participants(f'@{GROUP_USERNAME}', filter=ChannelParticipantsAdmins):
             auth.append(x.id)
    if event.sender_id in auth:
        x = await bot.get_messages(event.chat_id, ids=event.message_id)
        xx = x.raw_text
        btns = [
            [Button.url("💠 Channel 💠", url=f"https://t.me/{CHANNEL_USERNAME}"),
            Button.url("⚜️ Group ⚜️", url=f"https://t.me/{GROUP_USERNAME}")],
            [Button.url(f'{BTN1_NAME}', url=f'{BTN1_LINK}'),
            Button.url(f'{BTN2_NAME}', url=f'{BTN2_LINK}')],
            [Button.url(f'{BTN3_NAME}', url=f'{BTN3_LINK}')]]
       
        await event.edit(f"**REJECTED**\n\n~~{xx}~~", buttons=[Button.inline("Request Rejected 🚫", data="ndone")])
        await tbot.send_message(GROUP_ID, f"**⚠️ Request Rejected By Admin !!**\n\n~~{xx}~~", buttons=btns)
    else:
        await event.answer("Who TF are you? This is for admins only..", alert=True, cache_time=0)
        
@tbot.on(events.callbackquery.CallbackQuery(data="unavl"))
async def delete_message(event):
    if not auth:
        async for x in bot.iter_participants(f'@{GROUP_USERNAME}', filter=ChannelParticipantsAdmins):
             auth.append(x.id)
    if event.sender_id in auth:
        x = await bot.get_messages(event.chat_id, ids=event.message_id)
        xx = x.raw_text
        btns = [
            [Button.url("💠 Channel 💠", url=f"https://t.me/{CHANNEL_USERNAME}"),
            Button.url("⚜️ Group ⚜️", url=f"https://t.me/{GROUP_USERNAME}")],
            [Button.url(f'{BTN1_NAME}', url=f'{BTN1_LINK}'),
            Button.url(f'{BTN2_NAME}', url=f'{BTN2_LINK}')],
            [Button.url(f'{BTN3_NAME}', url=f'{BTN3_LINK}')]]
       
        await event.edit(f"**UNAVAILABLE**\n\n~~{xx}~~", buttons=[Button.inline("❗ Unavailable ❗", data="navl")])
        await tbot.send_message(GROUP_ID, f"**⚠️ Request Unavailable ⚠️**\n\n~~{xx}~~", buttons=btns)
    else:
        await event.answer("Who TF are you? This is for admins only..", alert=True, cache_time=0)
        
        
@tbot.on(events.callbackquery.CallbackQuery(data="isdone"))
async def isdone(e):
    if not auth:
        async for x in bot.iter_participants(f'@{GROUP_USERNAME}', filter=ChannelParticipantsAdmins):
             auth.append(x.id)
    if e.sender_id in auth:
        x = await bot.get_messages(e.chat_id, ids=e.message_id)
        xx = x.raw_text
        btns = [
            [Button.url("💠 Channel 💠", url=f"https://t.me/{CHANNEL_USERNAME}"),
            Button.url("⚜️ Group ⚜️", url=f"https://t.me/{GROUP_USERNAME}")],
            [Button.url(f'{BTN1_NAME}', url=f'{BTN1_LINK}'),
            Button.url(f'{BTN2_NAME}', url=f'{BTN2_LINK}')],
            [Button.url(f'{BTN3_NAME}', url=f'{BTN3_LINK}')]]
       
        await e.edit(f"**COMPLETED**\n\n~~{xx}~~", buttons=[Button.inline("Request Completed ✅", data="donne")])
        await tbot.send_message(GROUP_ID, f"**Request Completed**\n\n~~{xx}~~", buttons=btns)
    else:
        await e.answer("Who TF are you? This is for admins only..", alert=True, cache_time=0)
        
    
@tbot.on(events.callbackquery.CallbackQuery(data="donne"))
async def ans(e):
    await e.answer("This Request Is Completed... Checkout  💖 @{CHANNEL_USERNAME}", alert=True, cache_time=0)
        
@tbot.on(events.callbackquery.CallbackQuery(data="navl"))
async def ans(e):
    await e.answer("This Request Is Marked Unavailable By Admins", alert=True, cache_time=0)
        
        
@tbot.on(events.callbackquery.CallbackQuery(data="ndone"))
async def ans(e):
    await e.answer("This Request is unavailable... Ask Admins in @{GROUP_USERNAME} for help. 💞", alert=True, cache_time=0)
