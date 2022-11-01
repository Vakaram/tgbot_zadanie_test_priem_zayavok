from psycopg2 import Error
import psycopg2


class PostgreSQL:
    def __init__(self, host, port, user, password, database):
        try:
            self.connection = psycopg2.connect(user=user,
                                               password=password,
                                               host=host,
                                               port=port,
                                               database=database
                                               )
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def add_name_surname(self, tg_id, name_surname):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                        INSERT INTO registration_tg_users (tg_id, name_surname)
                        VALUES(%s, %s)
                        """,
                           (tg_id, name_surname,))
            self.connection.commit()
            print('Сохранил имя человека в БД')

    def add_phone(self, tg_id, phone): #вставляет значения к соответствующему tg id
        with self.connection.cursor() as cursor:
            cursor.execute("""
                        Update registration_tg_users phone = '%s' WHERE tg_id = '%s'
                        VALUES(%s, %s,)
                        """,
                           (phone, tg_id,))
            self.connection.commit()
        print('Телефон соответствует я добавил его в бд')

    def check_in_bd(self, tg_id):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT tg_id FROM registration_tg_users WHERE tg_id = %s",
                    (tg_id,)
            )
            self.connection.commit()
            proverka = cursor.fetchall()
            print(str(proverka) + 'если есть id то он есть в БД')
            if proverka:
                print("Пользователь есть в БД вижу это по базе")
                return True
            else:
                print('Пользователя нет в БД вижу это по базе')
                return None


    #
    # def del_user(self, id):
    #     delete_query = f"DELETE FROM `user` WHERE id = {id}"
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(delete_query)
    #         self.connection.commit()
    #
    # def update_age_by_id(self, new_age, id):
    #     update_query = f"UPDATE `user` SET age = {new_age} WHERE id = {id}"
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(update_query)
    #         self.connection.commit()
    #
    # def select_all_data(self):
    #     select_all_rows = f"SELECT * FROM `user`"
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(select_all_rows)
    #         rows = cursor.fetchall()
    #         return rows


# нужна переменная для создания бд по классу
host = '127.0.0.1'
port = "5432"
user = "postgres"
password = "admin"
database = "tg_bot_priyom_zayavok"

bd_add_delete_update = PostgreSQL(host=host, port=port, user=user, password=password, database=database)
