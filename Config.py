import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "LOVELYR_OBOT")
    LOVELY_SUPPORT = os.environ.get("LOVELY_SUPPORT", "LOVELYAPPEAL")
    LOVELY_CHANNEL = os.environ.get("LOVELY_CHANNEL", "ABOUTVEDMAT")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")


