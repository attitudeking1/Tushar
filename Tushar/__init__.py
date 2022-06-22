import os

from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


from Config import Config
BOT_USERNAME = Config.BOT_USERNAME

bot = TelegramClient('Tushar', api_id=Config.API_ID, api_hash=Config.API_HASH)
Tushar = bot.start(bot_token=Config.BOT_TOKEN)
