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
    return markup #нужен обязательно )
    print('Я дошёл до конца в создание основного меню ')

def buttons_main_ostavitzayavka_podelitsa_nazad():  # просто создаю менюшку
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📛 Оставить заявку")
    btn2 = types.KeyboardButton("🔔 Поделиться предложением")
    markup.add(btn1, btn2)
    btn3 = types.KeyboardButton("🛅 Назад")
    markup.add(btn3)
    return markup
    print('Я дошёл до конца в создание кнопок ЗАЯВКЕ ')

def buttons_svazatsa():  # создаю inline knopki для связаться
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Перезвоните мне", callback_data='perezvonite_mne')
    btn2 = types.InlineKeyboardButton("Свяжитесь со мнйо в чат-боте", callback_data='svaz_so_mnoy_v_chat_bote')
    btn3 = types.InlineKeyboardButton("Назад", callback_data='nazad_iz_svarhites_so_mnoy')
    markup.add(btn1, btn2, btn3)
    return markup




