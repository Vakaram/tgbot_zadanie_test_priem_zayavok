
import telebot  # telebot
from telebot import types  # для указание типов
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup  # States
from telebot.storage import StateMemoryStorage
from buttons.buttons import buttons_main_menu, buttons_main_ostavitzayavka_podelitsa_nazad, buttons_svazatsa
from create_bot import telebot_test
from database.CREATE_DATABASE import create_database_tg_bot_priyom_zayavok
from database.add_delete_update_table import PostgreSQL, bd_add_delete_update
from database.create_table import create_database_all
from psycopg2 import Error
import logging
import re
import time

print('Бот запущен запустился')

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(telebot_test, state_storage=state_storage)

create_database_tg_bot_priyom_zayavok()#создаём основную и пока единственную базу данных
# time.sleep(1)
# #не работает друг за другом почему то хм надо будет потом разобраться
# create_database_all.create_table_registration_tg_users() #основная таблица имя фам телефон id
# time.sleep(1)
#
# create_database_all.create_table_zayavka_tg_users() #зависимая таблица от основной по id
#

class MyStates(StatesGroup):
    name = State()
    phone = State()
    zayavka_step1 = State()
    zayavka_step2 = State()
    zayavka_step3 = State()



@bot.message_handler(commands=['start'])
def start_ex(message):
    tg_id = message.from_user.id
    if bd_add_delete_update.check_in_bd(tg_id) is True:                    # проверил пользователя теперь, если его нет предлагаю зарегаться и как успешно выдам ему клавиатуру, а если он есть, и просто удалил когда то чат, то выдаю кнопки
        print('Я вижу после сравнения что он есть в бд')
        bot.delete_state(message.from_user.id,message.chat.id)              # добавил 29.10 потомучто состояние надо было чистить чтобы код дальше шагал
        #ниже вызываем отпрвку смс в markup передаём нашу функцию с кнопками
        bot.send_message(message.chat.id,text="Привет, {0.first_name}! Раз ты уже зарегался я могу показать тебе клавиатуру".format(
                            message.from_user), reply_markup=buttons_main_menu())
    else:
        print('Я вижу после сравнения что его нет в бд')
        bot.send_message(message.chat.id, 'Введите имя')
        bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
        print('я перевёл его в другое состояние name')

@bot.message_handler(state="*", commands=['/cancel'])  # отмена любого состояния (типо не вводить, выйти при написаниее cancel
def any_state(message):
    bot.send_message(message.chat.id, "Отмена регистрации, для регистрации нажмите введите /start ")
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.name)
def name_get(message):
    regular_phone = r'^[А-Я]{1}[а-я]{1,100}\s[А-Я]{1}[а-я]{1,100}$'
    tg_id = message.from_user.id
    name_surname = message.text
    if re.match(regular_phone, name_surname) is not None:  # в тру меняем состояние на след дописываем данные в хранилище
        bot.set_state(message.from_user.id, MyStates.phone, message.chat.id)
        bot.send_message(message.chat.id, 'Введите телефон +7 без пробелов:', parse_mode='html')
        bd_add_delete_update.add_name_surname(tg_id,name_surname)
    else:
        bot.set_state(message.from_user.id, MyStates.name, message.chat.id)
        bot.send_message(message.chat.id, 'Имя должно быть Пример Иван Иванов :', parse_mode='html')
        print('Не подходит Имя ')

@bot.message_handler(state=MyStates.phone)  # просим телефон
def ready_for_answer(message):
    phone = message.text
    tg_id = message.from_user.id
    regular_phone = r'[+][7][0-9]{10}$'
    if re.match(regular_phone, phone) is not None:
        bd_add_delete_update.add_phone(tg_id,phone)
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.send_message(message.chat.id, #создал меню в общем.
                         text="Привет, {0.first_name}! Раз ты уже зарегался я могу показать тебе клавиатуру".format(
                             message.from_user), reply_markup=buttons_main_menu())
    else:
        bot.send_message(message.chat.id, 'Не подходит телефон надо +7 и всего 11 цифр:', parse_mode='html')
        bot.set_state(message.from_user.id, MyStates.phone, message.chat.id)
        print('Не подходит телефон ')

@bot.message_handler(state=MyStates.zayavka_step1)
def zayavka_step1(message): #класс,то что спрашиваем и шаг действующий
    print("Я внутри 1 шааг ")
    location = message.text #надо записать его и записать id )
    bot.send_message(message.chat.id, 'Шаг 2/3: Прикрепите фотографию или видео к своей заявке', parse_mode='html')
    bot.set_state(message.from_user.id, MyStates.zayavka_step2, message.chat.id)
    #Вызвать inline кнопку создам пожалуй

@bot.message_handler(state=MyStates.zayavka_step2)
def zayavka_step1(message): #класс,то что спрашиваем и шаг действующий
    print("Я внутри 2 шааг ")
    location = message.text #надо записать его и записать id )
    bot.send_message(message.chat.id, 'Шаг 3/3: Напишите причину обращения в подробностях ', parse_mode='html')
    bot.set_state(message.from_user.id, MyStates.zayavka_step3, message.chat.id)
    #Вызвать inline кнопку создам пожалуй

@bot.message_handler(state=MyStates.zayavka_step3)
def zayavka_step1(message): #класс,то что спрашиваем и шаг действующий
    print("Я внутри 3 шааг ")
    location = message.text #надо записать его и записать id )
    bot.send_message(message.chat.id, 'Жалоба отправлена администрации', parse_mode='html')
    bot.set_state(message.from_user.id, MyStates.zayavka_step2, message.chat.id)
    bot.delete_state(message.from_user.id, message.chat.id)
    #Вызвать inline кнопку создам пожалуй





@bot.message_handler()  # Эта штука должны быть в самом низу, она забирает ответы на классы сучка
def ostavit_zayavka(message):
    if message.text == '📛 Заявка':
        bot.send_message(message.chat.id, 'Ты только что нажал Заявка')
        bot.send_message(message.chat.id,  # создал меню в общем.
                         text="Вы нажали кнопку заявка, должно появится новое меню. ".format(
                             message.from_user), reply_markup=buttons_main_ostavitzayavka_podelitsa_nazad())
        print('Я ХЕНДЛЕРОМ который видет текст увидил ЗАЯВКА')
    elif message.text == '🛅 Назад':
        bot.send_message(message.chat.id,  # создал меню в общем.
                         text="Привет, {0.first_name}! Раз ты уже зарегался я могу показать тебе клавиатуру".format(
                             message.from_user), reply_markup=buttons_main_menu())
    elif message.text == '📞 Связь':
        bot.send_message(message.chat.id,  # создал меню в общем.
                         text="Привет, {0.first_name}! Раз ты уже зарегался я могу показать тебе клавиатуру".format(
                             message.from_user), reply_markup=buttons_svazatsa())
    elif message.text == '⚙ Настройки':
        pass
    elif message.text == '📛 Оставить заявку':
        bot.set_state(message.from_user.id, MyStates.zayavka_step1, message.chat.id)
        bot.send_message(message.chat.id, 'ШАГ 1/3. Напишите адрес или ориентир проблемы...')
    elif message.text == '☎ Полезные контакты':
        pass
    elif message.text == '🔔 Поделиться предложением':
        pass


@bot.callback_query_handler(func=lambda call:True)
def otveti_na_inline_knopki(call):
    if call.message:
        if call.data == 'perezvonite_mne':
            bot.send_message(call.message.chat.id, ' Я вижу вы нажали перезвонить Вам!')
        elif call.data == 'svaz_so_mnoy_v_chat_bote':
            bot.send_message(call.message.chat.id, ' Я вижу вы нажали Связаться в чате!')
        elif call.data == 'nazad_iz_svarhites_so_mnoy':
            bot.send_message(call.message.chat.id, ' Я вижу вы нажали назад Inline кнопка!')
            bot.send_message(call.message.chat.id,  # создал меню в общем.
                             text="Мы отменили ввод,выберите команду из меню ниже".format(
                                 call.message.from_user), reply_markup=buttons_main_menu())



# @bot.message_handler(state=MyStates.svazatsa)
# def ready_for_answer(message):
#     bot.send_message(message.chat.id, "Я попал в состояние заявки")




bot.add_custom_filter(custom_filters.StateFilter(bot))  # хм чтоже делают это два фильтра надобы узнать
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling(skip_pending=True)
