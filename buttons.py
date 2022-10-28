def buttons_main_menu():
    from telebot import types  # для указание типов #если в main указан он его не видит, поэтому тут импортирую что поделать
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