from telegram import ReplyKeyboardMarkup, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import  CallbackContext
import json

def start(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup([
        ["Menu"]
    ], resize_keyboard = True)
    text = "Assalomu alaykum 🖐🖐🖐 Xush kelibsiz!!!"
    context.bot.sendMessage(chat_id = update.message.chat_id, text=text, reply_markup = keyboard )

    print(update.message.text)

def fanlar(update: Update, context: CallbackContext):
    keyboard= ReplyKeyboardMarkup([
        ["Fanlarga yozilish"],
        ["Fanlar haqida"]
    ], resize_keyboard = True)
    context.bot.sendMessage(chat_id = update.message.chat_id, text="Bo'limni tanlang", reply_markup = keyboard)
    print(update.message.text)

def tanlov_fanlar(update : Update, context: CallbackContext):
    chat_id = update.message.chat.id
    markup = ReplyKeyboardMarkup([
        ['Pedagogika psixologiya','Biznes boshqaruv'],
        ['Satsiologiya','Fuqorolik jamyati'],
        ["Asosiy bo'lim"]
    ],resize_keyboard = True)
    context.bot.sendMessage(chat_id, text = "Tanlov fanlar", reply_markup = markup)
    
    print(update.message.chat_id)
def pedagogika(update:Update, context:CallbackContext):
    text = f"Fan o'qituvchisi: Irisbayeva M.\
        \nFan krediti: 4.0       \
    \nMashg'ulot: \
        \n      Ma'ruza: 30 soat,\
        \n      Amaliy: 30 soat.\
        \n      Mustaqil ta'lim: 60 soat,\
    \nNazorat turi:\
        \n      Joriy nazorat: 20 ball,\
        \n      Oraliq nazorat: 30 ball,\
        \n      Yakuniy nazorat:50 ball,\
        \n      Umumiy: 100 ball"
    context.bot.send_message(chat_id = update.message.chat_id, text=text)
def biznes(update:Update, context:CallbackContext):
    text = f"Fan o'qituvchisi: Axmedjanov A.\
        \nFan krediti: 4.0       \
    \nMashg'ulot: \
        \n      Ma'ruza: 30 soat,\
        \n      Amaliy: 30 soat.\
        \n      Mustaqil ta'lim: 60 soat,\
    \nNazorat turi:\
        \n      Joriy nazorat: 20 ball,\
        \n      Oraliq nazorat: 30 ball,\
        \n      Yakuniy nazorat:50 ball,\
        \n      Umumiy: 100 ball"
    context.bot.send_message(chat_id = update.message.chat_id, text=text)
def satsiologiya(update:Update, context:CallbackContext):
    text = f"Fan o'qituvchisi: Smatov X.\
        \nFan krediti: 4.0       \
    \nMashg'ulot: \
        \n      Ma'ruza: 30 soat,\
        \n      Amaliy: 30 soat.\
        \n      Mustaqil ta'lim: 60 soat,\
    \nNazorat turi:\
        \n      Joriy nazorat: 20 ball,\
        \n      Oraliq nazorat: 30 ball,\
        \n      Yakuniy nazorat:50 ball,\
        \n      Umumiy: 100 ball"
    context.bot.send_message(chat_id = update.message.chat_id, text=text)
def fuqorolik(update:Update, context:CallbackContext):
    # emoji  ="U+1F44C"
    text = f"Fan o'qituvchisi: Usmonov F.\
        \nFan krediti: 4.0       \
    \nMashg'ulot: \
        \n      Ma'ruza: 30 soat,\
        \n      Amaliy: 30 soat.\
        \n      Mustaqil ta'lim: 60 soat,\
    \nNazorat turi:\
        \n      Joriy nazorat: 20 ball,\
        \n      Oraliq nazorat: 30 ball,\
        \n      Yakuniy nazorat:50 ball,\
        \n      Umumiy: 100 ball " 
    context.bot.send_message(chat_id = update.message.chat_id, text=text)

    
def yozilish(update:Update, context: CallbackContext):
    chat_id=update.message.chat.id
    question="Bu semestr davomida qaysi tanlov fanini o'qimoqchisiz???",
    option = json.dumps([ "Pedagogika psixologiya","Biznes boshqaruv","Satsiologiya","Fuqorolik jamyati"])
    context.bot.sendPoll(chat_id = chat_id, question=question, options=option, is_anonymous = False, open_period = 60, protect_content = True)
    first_name = update.message.chat.first_name
    print(first_name)

def Fanga_yozilgan(update:Update, context:CallbackContext):
    pass

