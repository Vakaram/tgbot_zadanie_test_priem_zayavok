#https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/custom_states.py
import telebot  # telebot
from telebot import types # для указание типов
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup  # States
from telebot.storage import StateMemoryStorage
from create_bot import telebot_test
from database.create_database import create_database_all
from database.add_table_values import *
from psycopg2 import Error
import logging
import re

def buttons_main_menu(message): #просто создаю менюшку
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📛 Заявка")
    btn2 = types.KeyboardButton("📞 Связь")
    markup.add(btn1, btn2)
    btn3 = types.KeyboardButton("⚙ Настройки")
    btn4 = types.KeyboardButton("☎ Полезные контакты")
    markup.add(btn3)
    markup.add(btn4)

    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Раз ты уже зарегался я могу показать тебе клавиатуру".format(message.from_user), reply_markup=markup)
    print('Я дошёл до конца в создание кнопок ')


print('Я запустился')

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(telebot_test,state_storage=state_storage)
create_database_all() #при первом запуске подключаемся к бд, создаём нужную таблицу(дальше их будет больше допишу с первичным ключём и без

class MyStates(StatesGroup):
    name = State()
    phone = State()

@bot.message_handler(commands=['start'])
def start_ex(message):
    def zapros_bd():
        try:
            id_tg_user = message.from_user.id
            connection = psycopg2.connect(user="postgres",
                                          # пароль, который указали при установке PostgreSQL
                                          password="admin",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="tg_bot_priyom_zayavok")
            connection.autocommit = True  # постояяно сам коммитит данные
            cursor = connection.cursor()
            proverka = cursor.execute(
                "SELECT id_tg FROM registration_tg_users WHERE id_tg = %s",
                (id_tg_user,)
            )
            proverka = cursor.fetchall()
            print(proverka)
            if proverka:
                print("Пользователь есть в БД вижу это по базе")
                return True
            else:
                print('Пользователя нет в БД вижу это по базе')
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
    #проверил пользователя теперь, если его нет предлагаю зарегаться и как успешно выдам ему клавиатуру, а если он есть, и просто удалил когда то чат, то выдаю кнопки
    if zapros_bd() is True:
        print('Я вижу после сравнения что он есть в бд')
        bot.delete_state(message.from_user.id, message.chat.id) #добавил 29.10 потомучто состояние надо было чистить чтобы код дальше шагал
        buttons_main_menu(message)
    else:
        print('Я вижу после сравнения что его нет в бд')
        bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
        bot.send_message(message.chat.id, 'Введите имя')
        @bot.message_handler(state="*", commands=['/cancel']) #отмена любого состояния (типо не вводить, выйти при написаниее cancel
        def any_state(message):
            bot.send_message(message.chat.id, "Отмена регистрации, для регистрации нажмите введите /start ")
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
                            bot.send_message(message.chat.id, 'Отлично вы сохранены поздравляем:', parse_mode='html')
                    except (Exception, Error) as error:
                        print("Ошибка при работе с PostgreSQL", error)
                    finally:
                        if connection:
                            connection.close()
                            print('bd закрыли')
                    print('Телефон соответствует')
                bot.delete_state(message.from_user.id, message.chat.id)
                buttons_main_menu(message) #если всё верно ввёл то я могу показать клавиатуру
            else:
                bot.send_message(message.chat.id, 'Не подходит телефон надо +7 и всего 11 цифр:', parse_mode='html')
                bot.set_state(message.from_user.id, MyStates.phone, message.chat.id)
                print('Не подходит телефон ')

        # TODO: Для этой части кода ,  поправить красивый текст
        bot.add_custom_filter(custom_filters.StateFilter(bot)) #хм чтоже делают это два фильтра надобы узнать
        bot.add_custom_filter(custom_filters.IsDigitFilter())

# @bot.message_handler()  # тут пошли ответы на кнопки
# def ostavit_zayavka(message):
#     if message.text == '📛 Заявка':
#         bot.send_message(message.chat.id, "Выбирай дальше попробую теперь поменять состояние тут ")
# #         bot.set_state(message.from_user.id, MyStates.zayavka, message.chat.id)
#
#
# @bot.message_handler(state=MyStates.zayavka) #с
# def ready_for_answer(message):
#     bot.send_message(message.chat.id, "Я попал в состояние заявки")


#
# btn1 = types.KeyboardButton("📛 Заявка")
#     btn = types.KeyboardButton("📞 Связь")
#     markup.add(btn1, btn2)
#     btn3 = types.KeyboardButton("⚙ Настройки")
#     btn4 = types.KeyboardButton("☎ Полезные контакты")






bot.infinity_polling(skip_pending=True)

