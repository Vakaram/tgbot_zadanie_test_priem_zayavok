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
    def create_application(self, tg_id): #Будем добавлять id пользователя и всё на первом шаге
        with self.connection.cursor() as cursor:
            cursor.execute("""
                        INSERT INTO users_tg_request (tg_id)
                        VALUES(%s)
                        """,
                           (tg_id,))
            self.connection.commit()
            print('Сохранил id человека в бд запрос от пользователя сразу ')

    def add_request_location(self, location, tg_id): #Будем добавлять id пользователя и всё на первом шаге
        with self.connection.cursor() as cursor:
            sql = """    
                        UPDATE users_tg_request SET location = %s WHERE tg_id = %s and filled = FALSE
                             """
            cursor.execute(sql, (location,tg_id))
            self.connection.commit()

    def add_request_media(self, photo_id, tg_id): #Будем добавлять id пользователя и всё на первом шаге
        with self.connection.cursor() as cursor:
            sql = """    
                        UPDATE users_tg_request SET photo_video = %s WHERE tg_id = %s and filled = FALSE
                             """
            cursor.execute(sql, (photo_id,tg_id))
            self.connection.commit()


    def add_request_description(self, description, tg_id):
        with self.connection.cursor() as cursor:
            sql = """    
            UPDATE users_tg_request SET description = %s ,filled = TRUE WHERE tg_id = %s and filled = FALSE
            
                    """
            cursor.execute(sql, (description, tg_id))
            self.connection.commit()

    def form_an_application(self):#как всё заполнили , формируем ответ из бд, вид - карточка
        pass

    def delete_last_request_user(self, tg_id):
        with self.connection.cursor() as cursor:#нам нужно будет дропать последнию запись обращение если нажали отмена в первой графе при вводе.
            sql = """    
                    Delete from users_tg_request where tg_id = %s and filled = FALSE
                        """
            cursor.execute(sql, (tg_id,))
            self.connection.commit()

    """Ниже код для "Предложить предложение" """
    def create_offer_onli_tg_id(self, tg_id): #Будем добавлять id пользователя
        with self.connection.cursor() as cursor:
            cursor.execute("""
                        INSERT INTO share_the_offer (tg_id)
                        VALUES(%s)
                        """,
                           (tg_id,))
            self.connection.commit()
            print('Сохранил id человека в бд запрос от пользователя сразу ')


    def add_data_share_the_offer_only_text(self, text, tg_id ): #Будем добавлять id пользователя и всё на первом шаге
        with self.connection.cursor() as cursor:
            sql = """    
                UPDATE share_the_offer SET offer = %s, filled = TRUE WHERE tg_id = %s and filled = FALSE
                """
            cursor.execute(sql, (text,tg_id))
            self.connection.commit()

    def add_data_share_the_offer_text_photo_video(self, text,photo_video, tg_id ): #Будем добавлять id пользователя и всё на первом шаге
        with self.connection.cursor() as cursor:
            sql = """    
                UPDATE share_the_offer SET offer = %s , photo_video = %s , filled = TRUE WHERE tg_id = %s and filled = FALSE
                """
            cursor.execute(sql, (text,photo_video,tg_id,))
            self.connection.commit()

    def delete_last_share_the_offer(self, tg_id):
        with self.connection.cursor() as cursor:#нам нужно будет дропать последнию запись обращение если нажали отмена в первой графе при вводе.
            sql = """    
                Delete from share_the_offer where tg_id = %s and filled = FALSE
                """
            cursor.execute(sql, (tg_id,))
            self.connection.commit()

    """ Здесь для смены Имени и Телефона"""
    def rename_user_bd(self,name_surname,tg_id):
        with self.connection.cursor() as cursor:
            sql = """    
                UPDATE registration_tg_users SET name_surname = %s WHERE tg_id = %s
                """
            cursor.execute(sql, (name_surname,tg_id,))
            self.connection.commit()
    def rename_phone_bd(self,phone,tg_id):
        with self.connection.cursor() as cursor:
            sql = """    
                UPDATE registration_tg_users SET phone = %s WHERE tg_id = %s
                """
            cursor.execute(sql, (phone,tg_id,))
            self.connection.commit()
    def checking_phone_from_contact(self,tg_id): #проверка номера телефона в бд, когда пользователь говорит свяжитесь со мной по телефону
        with self.connection.cursor() as cursor:
            print(tg_id)
            sql = """    
                  SELECT phone From registration_tg_users WHERE tg_id = %s
                  """
            cursor.execute(sql, (tg_id,))
            result_phone = cursor.fetchall()[0][0]
            self.connection.commit()
            return result_phone









host = '127.0.0.1'
port = "5432"
user = "postgres"
password = "admin"
database = "tg_bot_priyom_zayavok"

bd_add_delete_update = PostgreSQL(host=host, port=port, user=user, password=password, database=database)

# tg_id = 1484570227
# print(bd_add_delete_update.checking_phone_from_contact(tg_id))