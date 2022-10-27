import psycopg2
from psycopg2 import Error
import logging


def registration_tg_users(self,id_tg_user,all_name_user,phone_user):
    self.zagluska = self
    self.id_tg_user = id_tg_user
    self.all_name_user = all_name_user
    self.phone_user = phone_user

    try:
        # Подключение к существующей базе данных
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
                (self.id_tg_user, self.all_name_user, self.phone_user)
            )
            logging.warning('Записал данные')
            # print('записал данные ') #можно вот это оставить

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            connection.close()
            print('bd закрыли')