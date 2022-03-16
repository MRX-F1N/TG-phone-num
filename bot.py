import telebot
from telebot import types # для указание типов
TOKEN ='5218153786:AAHECxTSSULAAAAF92gbb0FDkJA2Rx6drbU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("❓ Найти номер")
    markup.add(btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот справочник по Раздольному".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "❓ Найти номер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Такси")
        btn2 = types.KeyboardButton("Гос")
        back = types.KeyboardButton("Доставки")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Сейчас найдем", reply_markup=markup)
    
    elif(message.text == "Такси"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn99 = types.KeyboardButton("Узиер")
        btn98 = types.KeyboardButton("Люкс")
        btn97 = types.KeyboardButton("Семерочка")
        btn96 = types.KeyboardButton("Пилот")
        btn95 = types.KeyboardButton("Амир")
        btn94 = types.KeyboardButton("Лидер")
        btn93 = types.KeyboardButton("Такси 24")
        backkk = types.KeyboardButton ("НАЗАД")
        markup.add(btn99, btn98, btn97, btn96, btn95, btn94, btn93, backkk)
        bot.send_message(message.chat.id, text="Сейчас найдем", reply_markup=markup)

    elif(message.text == "Узиер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn14 = types.KeyboardButton("777")
        btn23 = types.KeyboardButton("Люкс")
        back = types.KeyboardButton("Доставки")
        markup.add(btn14, btn23, back)
        bot.send_message(message.chat.id, text="+797876646883", reply_markup=markup)

    elif (message.text == "НАЗАД"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Такси")
        btn2 = types.KeyboardButton("Гос")
        back = types.KeyboardButton("Доставки")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)














    elif message.text == "Доставки":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)