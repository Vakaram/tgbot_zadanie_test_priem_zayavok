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
#
#
# @bot.message_handler(commands=['start'])
# def start_ex(message):
#     print('Я вижу после сравнения что его нет в бд')
#     bot.set_state(message.from_user.id, State_Ostavit_Zayavky.shag1, message.chat.id)
#     bot.send_message(message.chat.id, 'ЗАПРОС ИНФЫ ')
# class State_Ostavit_Zayavky(StatesGroup):
#     shag1 = State()
#     shag2 = State()
#     shag3 = State()
#     shag4 = State()
#
#
#
# @bot.message_handler(state=State_Ostavit_Zayavky.shag1)
# def zayavka_adres_shag1(message): #класс,то что спрашиваем и шаг действующий
#     print('Я ХЕНДЛЕРОМ который есть шаг1 ,я сюда дошёл ? ')
#     bot.send_message(message.chat.id, 'Напишите адрес и свою проблему', parse_mode='html') #после добавить инлайн кнопки
#     adres = message.text
#     bot.set_state(message.from_user.id, State_Ostavit_Zayavky.shag2, message.chat.id)
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#             data['adres'] = message.text
# #тут шаги для приёма заявки левое меню с инлайнами
#
#
# @bot.message_handler(state=State_Ostavit_Zayavky.shag2)
# def zayavka_photo_video_shag2(message):
#     seychas_napisali = message.text
#     print(seychas_napisali)
#     bot.send_message(message.chat.id, 'Прикрепите фотку или видео ', parse_mode='html')
#     bot.set_state(message.from_user.id, State_Ostavit_Zayavky.shag3, message.chat.id) #надо брать id файла(фото,видео) из телеграм json или
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['photo_video'] = message.text
# @bot.message_handler(state=State_Ostavit_Zayavky.shag3)
# def zayavka_shag3(message):
#     seychas_napisali = message.text
#     print(seychas_napisali)
#     bot.send_message(message.chat.id, 'Напишите причину вашего обращения,опишите проблему', parse_mode='html')
#     bot.set_state(message.from_user.id, State_Ostavit_Zayavky.shag4, message.chat.id)
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['prichina_obrasheniya'] = message.text
# @bot.message_handler(state=State_Ostavit_Zayavky.shag4)
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
#     bot.delete_state(message.from_user.id, message.chat.id)
#
#
#
#
#
# bot.add_custom_filter(custom_filters.StateFilter(bot))  # хм чтоже делают это два фильтра надобы узнать
# bot.add_custom_filter(custom_filters.IsDigitFilter())
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
