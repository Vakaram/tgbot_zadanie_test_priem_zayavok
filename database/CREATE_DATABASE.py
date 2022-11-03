import psycopg2
from psycopg2 import Error

def create_database_tg_bot_priyom_zayavok():
    try:
        connection = psycopg2.connect(user="postgres",
                                           password="admin",
                                           host='127.0.0.1',
                                           port="5432"
                                           )
        connection.autocommit = True
        with connection.cursor() as cursor:
            sql = """CREATE database tg_bot_priyom_zayavok"""
            cursor.execute(sql)
            connection.commit()
            print('Создал бд проверь) ')
            connection.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
