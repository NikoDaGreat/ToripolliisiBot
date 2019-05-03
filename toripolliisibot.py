# -*- coding: utf-8 -*-
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import os
from urllib.request import urlretrieve
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# API-avain
token = os.environ['TGTORI_TOKEN']

def start(bot, update):
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id,
                    'Tervetuloa käyttämään Oulun Kauppatorin livekameran Telegram-bottia! Livefeedi löytyy Oulun kaupungin sivuilta osoitteesta https://www.ouka.fi/oulu/oulu-tietoa/nettikamerat')


def toripolliisi(bot, update):
    chat_id = update.message.chat.id
    urlretrieve("http://www.oulunkaupunki.fi/_private/kamera/picture1.jpg", "tori.jpg")
    img = Image.open("tori.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("TitilliumWeb-Bold.ttf", 38)
    x, y = 1320, 510
    filliColour="black"
    teksti="Toripolliisi"
    draw.text((x-1, y-1), teksti, font=font, fill=filliColour)
    draw.text((x+1, y-1), teksti, font=font, fill=filliColour)
    draw.text((x-1, y+1), teksti, font=font, fill=filliColour)
    draw.text((x+1, y+1), teksti, font=font, fill=filliColour)
    draw.text((x, y),teksti,(255,255,255),font=font)
    draw.ellipse((x+20, y+20, x-180, y-180), outline ='red')
    img.save('tori-teksti.jpg')
    bot.send_photo(chat_id, photo=open('tori-teksti.jpg', 'rb'))


def handle_message(bot, update):
    if update.message.text:
        words = update.message.text.split()
        words = list(map(lambda x: x.lower(), words))
        if "toripolliisi" in words:
            toripolliisi(bot, update)


updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('toripolliisi', toripolliisi))
updater.dispatcher.add_handler(MessageHandler(Filters.all, handle_message))
updater.start_polling()
updater.idle()
