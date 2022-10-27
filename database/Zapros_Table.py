import psycopg2
from psycopg2 import Error

def zapros_info_in_table():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="tg_bot_priyom_zayavok")
        connection.autocommit = True  # постояяно сам коммитит данные
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from registration_tg_users" #менять таблицу тут

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Phone  = ", row[2], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



def zapros_info_in_table_yestli_user():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="tg_bot_priyom_zayavok")
        connection.autocommit = True  # постояяно сам коммитит данные
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from registration_tg_users" #менять таблицу тут

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        print(type(mobile_records))
        print(mobile_records)
        id_tg_user = message.from_user.id
        for user in mobile_records:
            if id_tg_user == user[0]:
                bot.send_message(message.chat.id, 'Я вижу что вы есть в нашей базе данных.Добро пожаловать')
            else:
                bot.send_message(message.chat.id, 'Похоже вас нету в базе данных')

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()

zapros_info_in_table_yestli_user()