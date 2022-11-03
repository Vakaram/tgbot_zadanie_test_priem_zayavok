import psycopg2
from psycopg2 import Error


def drop_database_tg_bot_priyom_zayavok():
    try:
        connection = psycopg2.connect(user="postgres",
                                           password="admin",
                                           host='127.0.0.1',
                                           port="5432"
                                           )
        connection.autocommit = True
        with connection.cursor() as cursor:
            sql = """DROP DATABASE tg_bot_priyom_zayavok"""
            cursor.execute(sql)
            connection.commit()
            print('Удалил базу данных полностью ')
            connection.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

drop_database_tg_bot_priyom_zayavok()
