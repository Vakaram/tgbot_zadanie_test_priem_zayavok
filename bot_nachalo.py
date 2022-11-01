import telebot
from create_bot import telebot_test #берём ключ к боту
from database.create_database import create_database_all

bot = telebot.TeleBot(telebot_test)
create_database_all() #при первом запуске подключаемся к бд, создаём нужную таблицу(дальше их будет больше допишу с первичным ключём и без


@bot.message_handler(commands=['start']) #отслеживаем команду, функцию называем также
def start(message):
    message_zapros_name = '🌞<b>Доброго времени суток</b>, бот создан ,' \
                    'чтобы обрабатывать заявки и обращения пользователей.' \
                    'Чтобы воспользоваться этим, пришлите для начала ' \
                    'Ваше <b>Имя</b> и <b>Фамилию</b>'
    sent = bot.send_message(message.chat.id, message_zapros_name, parse_mode='html') #в этот чат отправляем текст (куда chat.id)
    bot.register_next_step_handler(sent, register_user )

def register_user(message): #функция получения текста и user_id
    name_register = message.text
    message_phone = '📞Теперь отпрвьте Ваш <b>номер телефона</b> через <b>+79998887766</b> следующим сообщением:'
    sent = bot.send_message(message.chat.id, message_phone, parse_mode='html')
    bot.register_next_step_handler(sent, register_phone)
    return name_register #возвратить по запросу

def register_phone(message):#функция получения телефона
    phone_user = message.text
    id_tg = message.from_user.id
    name_register = register_user(message)
    print(id_tg)
    print(phone_user)
    print(name_register)
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres", #попробовать вынести в функцию.
                                      # пароль, который указали при установке PostgreSQL
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="tg_bot_priyom_zayavok")
        connection.autocommit = True  # постояяно сам коммитит данные

        with connection.cursor() as cursor:  # добавляем данные в бд
            cursor.execute(
                """
                INSERT INTO registration_tg_users (id_tg, all_name, phone)
                VALUES('id_tg','phone_user','name_register');
                """
            )
            print('[INFO] Таблица создана,или уже существует')

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection:
            connection.close()
            print('bd закрыли')


bot.polling(non_stop=True) #запуск бота постоянно








