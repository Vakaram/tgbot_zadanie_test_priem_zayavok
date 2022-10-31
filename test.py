# # https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/custom_states.py
#
# import telebot  # telebot
# from telebot import types  # для указание типов
# from telebot import custom_filters
# from telebot.handler_backends import State, StatesGroup  # States
# from telebot.storage import StateMemoryStorage
# from create_bot import telebot_test
# from database.create_database import create_database_def
# from database.add_table_values import *
# from psycopg2 import Error
# import logging
# import re
# # ща будем тянуть импорты
# #надо было сразу делать requarements сейчас сделаю
#
#
# def buttons_main_menu(message):  # просто создаю менюшку
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("📛 Заявка")
#     btn2 = types.KeyboardButton("📞 Связь")
#     markup.add(btn1, btn2)
#     btn3 = types.KeyboardButton("⚙ Настройки")
#     btn4 = types.KeyboardButton("☎ Полезные контакты")
#     markup.add(btn3)
#     markup.add(btn4)
#     bot.send_message(message.chat.id,
#                      text="Привет, {0.first_name}! Раз ты уже зарегался я могу показать тебе клавиатуру".format(
#                          message.from_user), reply_markup=markup)
#     print('Я дошёл до конца в создание кнопок ')
#
# def buttons_main_ostavitzayavka_podelitsa_nazad(message):  # просто создаю менюшку
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("📛 Оставить заявку")
#     btn2 = types.KeyboardButton("🔔 Поделиться предложением")
#     markup.add(btn1, btn2)
#     btn3 = types.KeyboardButton("🛅 Назад")
#     markup.add(btn3)
#     bot.send_message(message.chat.id,
#                      text="Это я в стадии оставить заявку или предложить и назад".format(
#                          message.from_user), reply_markup=markup)
#     print('Я дошёл до конца в создание кнопок ')
#
#
# def buttons_svazatsa(message):#создаю inline knopki для связаться
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     btn1 = types.InlineKeyboardButton("Перезвоните мне", callback_data='perezvonite_mne')
#     btn2 = types.InlineKeyboardButton("Свяжитесь со мнйо в чат-боте", callback_data='svaz_so_mnoy_v_chat_bote')
#     btn3 = types.InlineKeyboardButton("Назад", callback_data='nazad_iz_svarhites_so_mnoy')
#     markup.add(btn1, btn2, btn3)
#     bot.send_message(message.chat.id,
#                      text="Ты нажаль Связаться ну вот тебе и меню".format(
#                          message.from_user), reply_markup=markup)
#
# def ostavi_zayavka_shag1(message):#создаю inline knopki для связаться
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     btn1 = types.InlineKeyboardButton("Перезвоните мне", callback_data='perezvonite_mne')
#     btn2 = types.InlineKeyboardButton("Свяжитесь со мнйо в чат-боте", callback_data='svaz_so_mnoy_v_chat_bote')
#     btn3 = types.InlineKeyboardButton("Назад", callback_data='nazad_iz_svarhites_so_mnoy')
#     markup.add(btn1, btn2, btn3)
#     bot.send_message(message.chat.id,
#                      text="Ты нажаль Связаться ну вот тебе и меню".format(
#                          message.from_user), reply_markup=markup)
#
# print('Бот запущен запустился')
#
# state_storage = StateMemoryStorage()
# bot = telebot.TeleBot(telebot_test, state_storage=state_storage)
# create_database_def()  # при первом запуске подключаемся к бд, создаём нужную таблицу(дальше их будет больше допишу с первичным ключём и без
#
# # class MyStates(StatesGroup):
# #     name = State()
# #     phone = State()
# #     # ostavit_zayavka = State()
#     # svazatsa = State() #связаться это когда нажал кнопку главного меню
#
#
# class State_ostavit_zayavky(StatesGroup):
#     shag1 = State()
#     shag2 = State()
#     shag3 = State()
#     shag4 = State()
# @bot.message_handler()
#
# @bot.message_handler(commands=['start'])
# def start_ex(message):
#     # bot.delete_state(message.from_user.id,message.chat.id)  # добавил 29.10 потомучто состояние надо было чистить чтобы код дальше шагал
#     bot.send_message(message.chat.id, 'Я в старте в предлагаю боту пойти в состояние  1  ')
#     bot.set_state(message.from_user.id, State_ostavit_zayavky.shag1,message.chat.id)
#     # buttons_main_menu(message)
#
#
# bot.add_custom_filter(custom_filters.StateFilter(bot))  # хм чтоже делают это два фильтра надобы узнать
# bot.add_custom_filter(custom_filters.IsDigitFilter())
#
#
#
#  # тут пошли ответы на кнопки
# def ostavit_zayavka(message):
#     if message.text == '📛 Заявка':
#         #тут статус не меняем пока не надо , а в кнопке Оставить заявку надо
#         bot.send_message(message.chat.id, 'Ты только что нажал Заявка')
#         buttons_main_ostavitzayavka_podelitsa_nazad(message)  # создаём новую клаву для этого меню
#         print('Я ХЕНДЛЕРОМ который видет текст увидил ЗАЯВКА')
#     elif message.text == '🛅 Назад':
#         buttons_main_menu(message)
#     elif message.text == '📞 Связь':
#         # bot.set_state(message.from_user.id, MyStates.svazatsa, message.chat.id)#тут поменяем состояния всё ок
#         buttons_svazatsa(message)
#     elif message.text == '⚙ Настройки':
#         pass
#     elif message.text == '☎ Полезные контакты':
#         pass
#     elif message.text == '📛 Оставить заявку':
#         # # bot.delete_state(message.from_user.id, message.chat.id)
#         # bot.send_message(message.chat.id, 'Ты только что нажал ОСТАВИТЬ ЗАЯВКУ ну тогда оставляй')
#         # # bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
#         # bot.set_state(message.from_user.id, State_ostavit_zayavky.shag1, message.chat.id)
#         # seychas_napisali = message.text
#         print('Я ХЕНДЛЕРОМ который видит текст увидел Оставить заявку ')
#     elif message.text == '🔔 Поделиться предложением':
#         pass
#
#
#
#
# @bot.message_handler(state=State_ostavit_zayavky.shag1)
# def zayavka_adres_shag1(message): #класс,то что спрашиваем и шаг действующий
#     print('Я ХЕНДЛЕРОМ который есть шаг1 ,я сюда дошёл ? ')
#     bot.send_message(message.chat.id, 'Напишите адрес и свою проблему', parse_mode='html') #после добавить инлайн кнопки
#     adres = message.text
#     bot.set_state(message.from_user.id, State_ostavit_zayavky.shag2, message.chat.id)
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['adres'] = message.text
# #тут шаги для приёма заявки левое меню с инлайнами
#
#
# @bot.message_handler(state=State_ostavit_zayavky.shag2)
# def zayavka_photo_video_shag2(message):
#     seychas_napisali = message.text
#     print(seychas_napisali)
#     bot.send_message(message.chat.id, 'Прикрепите фотку или видео ', parse_mode='html')
#     bot.set_state(message.from_user.id, State_ostavit_zayavky.shag3, message.chat.id) #надо брать id файла(фото,видео) из телеграм json или
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['photo_video'] = message.text
# @bot.message_handler(state=State_ostavit_zayavky.shag3)
# def zayavka_shag3(message):
#     seychas_napisali = message.text
#     print(seychas_napisali)
#     bot.send_message(message.chat.id, 'Напишите причину вашего обращения,опишите проблему', parse_mode='html')
#     bot.set_state(message.from_user.id, State_ostavit_zayavky.shag4,message.chat.id)
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['prichina_obrasheniya'] = message.text
# @bot.message_handler(state=State_ostavit_zayavky.shag4)
# def zayavka_shag3(message):
#     seychas_napisali = message.text
#     print(seychas_napisali)
#     bot.send_message(message.chat.id, 'Ваше обраение зарегестрированно', parse_mode='html')
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         sobral_zayavku = \
#               (f"name: {data['adres']}\n"
#                f"phone: {data['photo_video']}\n"
#                f"phone: {data['prichina_obrasheniya']}\n")
#         print(sobral_zayavku)
#
#
#
# @bot.callback_query_handler(func=lambda call:True)
# def otveti_na_inline_knopki(call):
#     if call.message:
#         if call.data == 'perezvonite_mne':
#             # bot.send_message(call.message.chat.id, ' Я вижу вы нажали перезвонить Вам!')
#             # bot.delete_state(message.from_user.id, message.chat.id)
#             bot.send_message(call.message.chat.id, 'Ты только что нажал ОСТАВИТЬ ЗАЯВКУ ну тогда оставляй')
#             # bot.set_state(call.message.from_user.id, MyStates.name, call.message.chat.id)
#             # bot.set_state(call.message.from_user.id, State_ostavit_zayavky.shag1, call.message.chat.id)
#             seychas_napisali = call.message.text
#             print('Я ХЕНДЛЕРОМ который видит текст увидел Оставить заявку ')
#         elif call.data == 'svaz_so_mnoy_v_chat_bote':
#             bot.send_message(call.message.chat.id, ' Я вижу вы нажали Связаться в чате!')
#         elif call.data == 'nazad_iz_svarhites_so_mnoy':
#             bot.send_message(call.message.chat.id, ' Я вижу вы нажали назад Inline кнопка!')
#             buttons_main_menu(call.message)
#
#
#
#         # TODO: Для этой части кода ,  поправить красивый текст
#
#
#
#
#
# # @bot.message_handler(state=MyStates.svazatsa)
# # def ready_for_answer(message):
# #     bot.send_message(message.chat.id, "Я попал в состояние заявки")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# bot.infinity_polling(skip_pending=True)




import telebot  # telebot

from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup  # States

# States storage
from telebot.storage import StateMemoryStorage

from create_bot import telebot_test

# Now, you can pass storage to bot.
state_storage = StateMemoryStorage()  # you can init here another storage

bot = telebot.TeleBot(telebot_test,
                      state_storage=state_storage)


# States group.
class MyStates(StatesGroup):
    # Just name variables differently
    name = State()  # creating instances of State class is enough from now
    surname = State()
    age = State()


@bot.message_handler(commands=['start'])
def start_ex(message):
    """
    Start command. Here we are starting state
    """
    bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
    bot.send_message(message.chat.id, 'Hi, write me a name')


# Any state
@bot.message_handler(state="*", commands=['cancel'])
def any_state(message):
    """
    Cancel state
    """
    bot.send_message(message.chat.id, "Your state was cancelled.")
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=MyStates.name)
def name_get(message):
    """
    State 1. Will process when user's state is MyStates.name.
    """
    bot.send_message(message.chat.id, 'Now write me a surname')
    bot.set_state(message.from_user.id, MyStates.surname, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text


@bot.message_handler(state=MyStates.surname)
def ask_age(message):
    """
    State 2. Will process when user's state is MyStates.surname.
    """
    bot.send_message(message.chat.id, "What is your age?")
    bot.set_state(message.from_user.id, MyStates.age, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['surname'] = message.text


# result
@bot.message_handler(state=MyStates.age, is_digit=True)
def ready_for_answer(message):
    """
    State 3. Will process when user's state is MyStates.age.
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        msg = ("Ready, take a look:\n<b>"
               f"Name: {data['name']}\n"
               f"Surname: {data['surname']}\n"
               f"Age: {message.text}</b>")
        bot.send_message(message.chat.id, msg, parse_mode="html")
    bot.delete_state(message.from_user.id, message.chat.id)


# incorrect number
@bot.message_handler(state=MyStates.age, is_digit=False)
def age_incorrect(message):
    """
    Wrong response for MyStates.age
    """
    bot.send_message(message.chat.id, 'Looks like you are submitting a string in the field age. Please enter a number')


# register filters

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling(skip_pending=True)
