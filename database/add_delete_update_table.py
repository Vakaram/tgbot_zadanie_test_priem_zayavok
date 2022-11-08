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

    def add_phone(self, tg_id, phone):  # вставляет значения к соответствующему tg id
        with self.connection.cursor() as cursor:
            sql = """    
            UPDATE registration_tg_users SET phone = %s WHERE tg_id = %s
                 """
            cursor.execute(sql, (phone, tg_id,))
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

"""Ниже идёт добавление к заявке , все 3 шага и дропы и делиты и т.д """
    def create_application(self, tg_id, name_surname): #Будем добавлять id пользователя и всё на первом шаге
        with self.connection.cursor() as cursor:
            cursor.execute("""
                        INSERT INTO registration_tg_users (tg_id, name_surname)
                        VALUES(%s, %s)
                        """,
                           (tg_id, name_surname,))
            self.connection.commit()
            print('Сохранил имя человека в БД')
    def add_application_location(self, location): #Будем добавлять id пользователя и всё на первом шаге
        with self.connection.cursor() as cursor:
            sql = """    
                UPDATE registration_tg_users SET phone = %s WHERE tg_id = %s
                     """
            cursor.execute(sql, (location,))
            self.connection.commit()

    def add_application_media(self, location, name_surname): #Будем добавлять id пользователя и всё на первом шаге
        with self.connection.cursor() as cursor:
            sql = """    
                UPDATE registration_tg_users SET phone = %s WHERE tg_id = %s
                     """
            cursor.execute(sql, (phone, tg_id,))
            self.connection.commit()
    def add_application_description(self, location, name_surname):
        with self.connection.cursor() as cursor: #добавить обращение, и изменить состояние на TRUE
            sql = """    
                UPDATE registration_tg_users SET phone = %s WHERE tg_id = %s
                     """
            cursor.execute(sql, (phone, tg_id,))
            self.connection.commit()

    def form_an_application(self):#как всё заполнили , формируем ответ из бд, вид - карточка
        pass

    def delete_last_request(self):
        pass #нам нужно будет дропать последнию запись обращение если нажали отмена в первой графе при вводе.


host = '127.0.0.1'
port = "5432"
user = "postgres"
password = "admin"
database = "tg_bot_priyom_zayavok"

bd_add_delete_update = PostgreSQL(host=host, port=port, user=user, password=password, database=database)
