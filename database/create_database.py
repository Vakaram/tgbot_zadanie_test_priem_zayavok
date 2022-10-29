import psycopg2
from psycopg2 import Error

def create_database_def():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="tg_bot_priyom_zayavok")
        connection.autocommit = True  # постояяно сам коммитит данные
        with connection.cursor() as cursor:  # просто запрос инфы о подключение
            cursor.execute(
                "SELECT version();"
            )
            print(f'Server version: {cursor.fetchone()}')
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(connection.get_dsn_parameters(), "\n")

        with connection.cursor() as cursor:  # создание таблицы если её нет
            cursor.execute(
                """
                CREATE TABLE registration_tg_users(
                    id_tg int PRIMARY KEY,
                    all_name varchar(150) NOT NULL,
                    phone varchar(20)
                    );
                """
            )
            print('[INFO] Таблица создана')

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            connection.close()
            print('bd закрыли')
# create_database_def()

