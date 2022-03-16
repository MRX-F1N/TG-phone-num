import telebot
import sqlite3
from telebot import types # для указание типов
TOKEN ='5218153786:AAGPGWx8B04v_2bhxUFpsx5JcmKCJTwvXWw'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    connect =sqlite3.connect('user.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""") 

    connect.commit()

    users_id = [message.chat.id]
    cursor.execute("INSERT INTO login_id VALUES(?);", users_id)
    connect.commit()



    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("❓ Найти номер")
    markup.add(btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот справочник по Раздольному. Я найду те номера котоыре тебе нужны. Что-бы найти нужный номер воспользуйся меню снизу".format(message.from_user), reply_markup=markup)
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEELNFiMYZ0UNswZewGJGxnKhzKOK_8ywACrwsAAv1pgUph8CTBF6FPxCME")

    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "❓ Найти номер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🚕Такси")
        btn2 = types.KeyboardButton("Гос")
        back = types.KeyboardButton("Доставки")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Сейчас найдем", reply_markup=markup)
    
    elif(message.text.lower() == "🚕такси"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn99 = types.KeyboardButton("🌟Узиер🌟")
        btn98 = types.KeyboardButton("🌟Люкс🌟")
        btn97 = types.KeyboardButton("🌟Семерочка🌟")
        btn96 = types.KeyboardButton("🌟Пилот🌟")
        btn95 = types.KeyboardButton("🌟Амир🌟")
        btn94 = types.KeyboardButton("🌟Лидер🌟")
        btn93 = types.KeyboardButton("🌟Такси 24🌟")
        backkk = types.KeyboardButton ("🔙 НАЗАД")
        markup.add(btn99, btn98, btn97, btn96, btn95, btn94, btn93, backkk)
        bot.send_message(message.chat.id, text="Сейчас найдем", reply_markup=markup)


    elif(message.text == "🌟Узиер🌟"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn98 = types.KeyboardButton("🌟Люкс🌟")
        btn97 = types.KeyboardButton("🌟Семерочка🌟")
        btn96 = types.KeyboardButton("🌟Пилот🌟")
        btn95 = types.KeyboardButton("🌟Амир🌟")
        btn94 = types.KeyboardButton("🌟Лидер🌟")
        btn93 = types.KeyboardButton("🌟Такси 24🌟")
        backkk = types.KeyboardButton ("🔙 НАЗАД")
        markup.add(btn98, btn97, btn96, btn95, btn94, btn93, backkk)
        bot.send_message(message.chat.id, text="[+79991234567](tel:+79991234567)", parse_mode='Markdown', reply_markup=markup)

    elif (message.text == "🔙 НАЗАД"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🚕Такси")
        btn2 = types.KeyboardButton("Гос")
        back = types.KeyboardButton("Доставки")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)














    elif message.text == "Доставки":
        bot.send_message(message.chat.id, text="Нету у нас их :D")
    
    elif (message.text.lower() == "меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("❓ Найти номер")
        btnhelp = types.KeyboardButton("🆘Помощь")
        markup.add(btn2, btnhelp)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)