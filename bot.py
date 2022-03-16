import telebot
import sqlite3
from telebot import types # для указание типов
TOKEN =''

bot = telebot.TeleBot(TOKEN)

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("❓ Найти номер")
    markup.add(btn2)
    bot.send_message(message.chat.id, text=f"Привет, {message.chat.username}! Я бот справочник по Раздольному. Я найду те номера котоыре тебе нужны. Что-бы найти нужный номер воспользуйся меню снизу".format(message.from_user), reply_markup=markup)
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEELNFiMYZ0UNswZewGJGxnKhzKOK_8ywACrwsAAv1pgUph8CTBF6FPxCME")

    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
        
    db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "❓ Найти номер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🚕Такси")
        btn2 = types.KeyboardButton("Гос")
        back = types.KeyboardButton("Доставки")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выбери категорию", reply_markup=markup)
    
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
        btn1 = types.KeyboardButton("🚕Такси")
        btn2 = types.KeyboardButton("Гос")
        back = types.KeyboardButton("Доставки")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "🆘Помощь"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("❓ Найти номер")
        markup.add(btn2)
        bot.send_message(message.chat.id, text="#Благодарим за использование Телеграм-бота для поиска информации по открытым источникам информации.    Наш бот очень прост в использовании", parse_mode='Markdown', reply_markup=markup)














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