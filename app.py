from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CallbackContext, CommandHandler, MessageHandler, Filters
import os
from main import start, fanlar, tanlov_fanlar, pedagogika, biznes, satsiologiya, fuqorolik, yozilish

TOKEN = os.environ["TOKEN"]
bot = Bot(TOKEN)

app = Flask("__name__")

@app.route('/home', methods = ["GET", "POST"])
def hello():
    if request.method == "GET":
        return 'hi this is bot onlline ovoz'
    elif request.method == "POST":
        
        #request majburiy obyekt ga o'tkazadi
        data = request.get_json(force = True)
        
        dispatcher: Dispatcher = Dispatcher(bot,None, workers=0)
        update: Update = Update.de_json(data, bot)
        
        
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(Filters.text("Menu"), fanlar))
        dispatcher.add_handler(MessageHandler(Filters.text("Asosiy bo'lim"), fanlar))
        dispatcher.add_handler(MessageHandler(Filters.text("Fanlar haqida"), tanlov_fanlar))
        dispatcher.add_handler(MessageHandler(Filters.text("Fanlarga yozilish"), yozilish))
        dispatcher.add_handler(MessageHandler(Filters.text("Pedagogika psixologiya"), pedagogika))
        dispatcher.add_handler(MessageHandler(Filters.text("Satsiologiya"), satsiologiya))
        dispatcher.add_handler(MessageHandler(Filters.text("Biznes boshqaruv"), biznes))
        dispatcher.add_handler(MessageHandler(Filters.text("Fuqorolik jamyati"), fuqorolik))

        
        dispatcher.process_update(update)
    return "ok"