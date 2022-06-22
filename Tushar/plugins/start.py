from Tushar import Tushar, BOT_USERNAME
from Config import Config
from telethon import events, Button

LOVELY_PM_START = """
Hi I'm simple group managing bot
"""

@Tushar.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,            
             Config.START_IMG,
             caption=LOVELY_PM_START.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ Add me to your group", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("🗣️ Support", f"https://t.me/{Config.LOVELY_SUPPORT}"), Button.url("📣 Updates", f"https://t.me/{Config.LOVELY_CHANNEL}")],
        [Button.inline("Commands", data="help")]])
       return

    if event.is_group:
       await event.reply(LOVELY_PM_START.format(event.sender.first_name), buttons=[
        [Button.url("➕ Add me to your group", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("🗣️ Support", f"https://t.me/{Config.LOVELY_SUPPORT}"), Button.url("📣 Updates", f"https://t.me/{Config.LOVELY_CHANNEL}")],
        [Button.inline("Commands", data="help")]])
       return



@Tushar.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(LOVELY_PM_START.format(event.sender.first_name), buttons=[
        [Button.url("➕ Add me to your group", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("🗣️ Support", f"https://t.me/{Config.LOVELY_SUPPORT}"), Button.url("📣 Updates", f"https://t.me/{Config.LOVELY_CHANNEL}")],
        [Button.inline("Commands", data="help")]])
       return
