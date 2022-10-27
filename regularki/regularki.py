import re

# s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
# result = re.match('dC',s)
# print(result)

# для телефон
# ^7 = искать в начале = можно в скобки занести в нижние будет отрицанием не с плюс семь начинаться
# /^[+7][0-9]{9}/gm
#
#
# имя и фамилия
# [0-9]любой символ из скобок или [А-Яа-я] любая буква
#^[А-Я]{1}[а-я]{1,100}\s[А-Я]{1}[а-я]{1,100}

name = 'ММакаров Владимир'
regular_phone = r'^[А-Я]{1}[а-я]{1,100}\s[А-Я]{1}[а-я]{1,100}$'
if re.match(regular_phone,name) is not None:
    print('Имя соответствует')
else:
    print('Не подходит Имя ')


phone = '+7(999)777-99-88'
regular_phone = r'[+][7][0-9]{10}$'
if re.match(regular_phone,phone) is not None:
    print('Телефон соответствует')
else:
    print('Не подходит телефон ')
