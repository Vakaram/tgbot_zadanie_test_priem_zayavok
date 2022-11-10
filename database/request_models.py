from psycopg2 import Error
import psycopg2


class UserInfoRequest:
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


    def callback_request_for_group(self,tg_id):  # проверка номера телефона в бд, когда пользователь говорит свяжитесь со мной по телефону
        with self.connection.cursor() as cursor:
            sql = """    
                SELECT rtu.tg_id, rtu.name_surname, rtu.phone, rtu.user_name_tg, to_char(cmb.date_create,'YYYY/MM/DD')   
                From registration_tg_users as rtu
                LEFT JOIN call_me_back as cmb on rtu.tg_id = cmb.tg_id
                WHERE rtu.tg_id = 1484570227
                ORDER BY cmb.date_create DESC 
                limit 1
                """
            cursor.execute(sql, (tg_id,))
            answer_select = cursor.fetchall()
            print(answer_select)
            all_text = 'Поступила просьба позвонить по телефону'+'\n' +str(answer_select[0][3]) +'\n' +'Имя и Фамилия:' + str(answer_select[0][1]) + '\n' + 'Телефон:' + str(answer_select[0][2]) + '\n' + 'Просит вас перезвонить.' + '\n' + 'Дата заявки: ' + str(answer_select[0][4])
            self.connection.commit()
            return all_text

host = '127.0.0.1'
port = "5432"
user = "postgres"
password = "admin"
database = "tg_bot_priyom_zayavok"

request_all_bd = UserInfoRequest(host=host, port=port, user=user, password=password, database=database)
# bd_add_delete_update.callback_request_for_group(tg_id=1484570227)


tg_id = 1484570227
print(request_all_bd.callback_request_for_group(tg_id))