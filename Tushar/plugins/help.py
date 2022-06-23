from telethon import events, Button
from Tushar import Tushar, BOT_USERNAME

btn =[
    [Button.inline("Admin", data="admin"), Button.inline("Bans", data="bans")],
    [Button.inline("Chat Cleaner", data="zombies"), Button.inline("Misc", data="misc")],
    [Button.inline("Locks", data="locks"), Button.inline("Pins", data="pins")],
    [Button.inline("Pugres", data="purges")],
    [Button.inline("Home", data="start")]]

HELP_TEXT = "Welcome To help Menu Section\n\nClick on the Buttons!"


@Tushar.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):

    if event.is_group:
       await event.reply("Contact me in PM to get available help menu!", buttons=[
       [Button.url("Help And Commands!", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Tushar.on(events.NewMessage(pattern="^/start help"))
async def _(event):

    await event.reply(HELP_TEXT, buttons=btn)

@Tushar.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)
