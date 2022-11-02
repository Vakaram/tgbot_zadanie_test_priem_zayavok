from telebot import types  # для указание типов

def buttons_main_menu():  # просто создаю менюшку
    print('Я вызвал создание кнопок')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📛 Заявка")
    btn2 = types.KeyboardButton("📞 Связь")
    markup.add(btn1, btn2)
    btn3 = types.KeyboardButton("⚙ Настройки")
    btn4 = types.KeyboardButton("☎ Полезные контакты")
    markup.add(btn3)
    markup.add(btn4)
    # bot.send_message(message.chat.id,
    #                  text="Привет, {0.first_name}! Раз ты уже зарегался я могу показать тебе клавиатуру".format(
    #                      message.from_user), reply_markup=markup)
    return markup
    print('Я дошёл до конца в создание основного меню ')

def buttons_main_ostavitzayavka_podelitsa_nazad(message,bot):  # просто создаю менюшку
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📛 Оставить заявку")
    btn2 = types.KeyboardButton("🔔 Поделиться предложением")
    markup.add(btn1, btn2)
    btn3 = types.KeyboardButton("🛅 Назад")
    markup.add(btn3)
    bot.send_message(message.chat.id,
                     text="Это я в стадии оставить заявку или предложить и назад".format(
                         message.from_user), reply_markup=markup)
    print('Я дошёл до конца в создание кнопок ')

def buttons_svazatsa(message,bot):  # создаю inline knopki для связаться
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Перезвоните мне", callback_data='perezvonite_mne')
    btn2 = types.InlineKeyboardButton("Свяжитесь со мнйо в чат-боте", callback_data='svaz_so_mnoy_v_chat_bote')
    btn3 = types.InlineKeyboardButton("Назад", callback_data='nazad_iz_svarhites_so_mnoy')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Ты нажаль Связаться ну вот тебе и меню".format(
                         message.from_user), reply_markup=markup)



