from psycopg2 import Error
import psycopg2
class CreateTableAll:
    def __init__(self, host, port, user, password, database):
        try:
            self.connection = psycopg2.connect(user=user,
                                               password=password,
                                               host=host,
                                               port=port,
                                               database=database
                                               )
            print('Я подключился к бд')
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def create_table_registration_tg_users(self):
        try:
            with self.connection.cursor() as cursor:  # создание таблицы если её нет
                cursor.execute(
                    """
                    CREATE TABLE registration_tg_users(
                        tg_id int PRIMARY KEY,
                        name_surname varchar(150) NOT NULL,
                        phone varchar(20),
                        is_admin boolean default FALSE
                        );
                    """
                )
                self.connection.commit() #обязательная штука даже в with
                print('[INFO] Таблица registration_tg_users создана')
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL с registration_tg_users" , error)

    def create_table_zayavka_tg_users(self):
        try:
            with self.connection.cursor() as cursor:  # создание таблицы если её нет
                cursor.execute(
                    """
                    CREATE TABLE users_tg_request(
                        application_id serial, 
                        tg_id int NOT NULL,
                        location varchar(150),
                        photo_video varchar(150),
                        description varchar (400),
                        filled boolean default FALSE, 
                        date_create timestamp NOT NULL default CURRENT_TIMESTAMP,
                        FOREIGN KEY (tg_id) REFERENCES registration_tg_users (tg_id)
                        );
                    """
                )
                self.connection.commit() #обязательная штука даже в with
                print('[INFO] Таблица zayavka_tg_users создана')
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL zayavka_tg_users ", error)





host = '127.0.0.1'
port = "5432"
user = "postgres"
password = "admin"
database = "tg_bot_priyom_zayavok"

create_database_all = CreateTableAll(host=host, port=port, user=user, password=password, database=database)

# create_database_all.create_table_registration_tg_users()
#
# create_database_all.create_table_zayavka_tg_users()




# create_database_all.create_table_registration_tg_users()
# create_database_all.create_table_zayavka_tg_users()




