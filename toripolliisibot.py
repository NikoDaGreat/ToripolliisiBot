# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler
import os

# API-avain
token = os.environ['TGTORI_TOKEN']

def start(bot, update):
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id,
                    'Tervetuloa käyttämään Oulun Kauppatorin livekameran Telegram-bottia! Livefeedi löytyy Oulun kaupungin sivuilta osoitteesta https://www.ouka.fi/oulu/oulu-tietoa/nettikamerat')


def toripolliisi(bot, update):
    pass

updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('toripolliisi', toripolliisi))
updater.start_polling()
updater.idle()
