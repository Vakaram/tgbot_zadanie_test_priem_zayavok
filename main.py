#https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/custom_states.py
import telebot  # telebot
from telebot import types # для указание типов
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup  # States
from telebot.storage import StateMemoryStorage
from create_bot import telebot_test
from database.create_database import create_database_def
from database.add_table_values import *
from psycopg2 import Error
import logging
import re


print('Я запустился')

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(telebot_test,state_storage=state_storage)
create_database_def() #при первом запуске подключаемся к бд, создаём нужную таблицу(дальше их будет больше допишу с первичным ключём и без

class MyStates(StatesGroup):
    name = State()
    phone = State()

@bot.message_handler(commands=['start'])
def start_ex(message):
    if #если в базе данных есть этот id телеги и все поля заполненны
    bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
    bot.send_message(message.chat.id, 'Введите имя')

@bot.message_handler(state="*", commands=['cancel']) #отмена любого состояния (типо не вводить, выйти при написаниее cancel
def any_state(message):
    bot.send_message(message.chat.id, "Your state was cancelled.")
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.name)
def name_get(message):
    regular_phone = r'^[А-Я]{1}[а-я]{1,100}\s[А-Я]{1}[а-я]{1,100}$'
    name_user = message.text
    if re.match(regular_phone, name_user) is not None: #в тру меняем состояние на след дописываем данные в хранилище
        bot.set_state(message.from_user.id, MyStates.phone, message.chat.id)
        bot.send_message(message.chat.id, 'Телефон:', parse_mode='html')
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = message.text
        print('Имя соответствует')
    else:
        bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
        bot.send_message(message.chat.id, 'Имя должно быть Пример Иван Иванов :', parse_mode='html')
        print('Не подходит Имя ')


@bot.message_handler(state=MyStates.phone) #просим телефон
def ready_for_answer(message):
    phone_user = message.text
    regular_phone = r'[+][7][0-9]{10}$'
    if re.match(regular_phone, phone_user) is not None:
        bot.send_message(message.chat.id, 'Отлично вы сохранены поздравляем:', parse_mode='html')
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['phone'] = message.text
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            msg = (f"name: {data['name']}\n"
                   f"phone: {data['phone']}\n")
            id_tg_user = message.from_user.id
            all_name_user = data['name']
            phone_user = data['phone']
            print(msg)
            print(id_tg_user)
        try:
            # Подключение к существующей базе данных
            connection = psycopg2.connect(user="postgres",
                                          password="admin",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="tg_bot_priyom_zayavok")
            connection.autocommit = True  # постояяно сам коммитит данные

            with connection.cursor() as cursor:  # добавляем данные в бд
                cursor.execute(
                    """
                    INSERT INTO registration_tg_users (id_tg, all_name, phone)
                    VALUES(%s, %s, %s)
                    """,
                    (id_tg_user, all_name_user, phone_user)
                )
                logging.warning('Записал данные')
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                connection.close()
                print('bd закрыли')
        print('Телефон соответствует')
    else:
        bot.send_message(message.chat.id, 'Не подходит телефон надо +7 и всего 11 цифр:', parse_mode='html')
        bot.set_state(message.from_user.id, MyStates.phone, message.chat.id)
        print('Не подходит телефон ')
    bot.delete_state(message.from_user.id, message.chat.id)
# TODO: Для этой части кода ,  поправить красивый текст
# TODO: Посмотреть по условию что если чел старт нажимает у него заново не спрашивало имя и телефон, а сразу была клава его со следующей стадией
# TODO: Если у него есть только номер, спрашивать имя или наоборот
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())





bot.infinity_polling(skip_pending=True)

