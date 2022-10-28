import telebot  # telebot
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup  # States
from telebot.storage import StateMemoryStorage
from create_bot import telebot_test
from database.create_database import create_database_def
from database.add_table_values import *
from psycopg2 import Error
import logging
import re
from telebot import types # для указание типов

print('Я запустился')

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(telebot_test,state_storage=state_storage)
print('Я создался')
@bot.message_handler(commands=['start'])
def start_ex(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📛 Заявка")
    btn2 = types.KeyboardButton("📞 Связь")
    markup.add(btn1, btn2)
    btn3 = types.KeyboardButton("⚙ Настройки")
    btn4 = types.KeyboardButton("☎ Полезные контакты")
    markup.add(btn3)
    markup.add(btn4)

    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=markup)
    print('Я дошёл до конца в создание кнопок ')

bot.infinity_polling(skip_pending=True)



















