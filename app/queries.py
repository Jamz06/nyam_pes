# Модуль с запросами

import pymysql.cursors
import datetime

# Универсальный Запрос под нужную таблицу. Выбрать все записи.
simple_query = """
    SELECT * FROM {table}
"""

# Универсальный запрос под нужную таблицу. Выбрать запись по ID
row_query = """
    SELECT * FROM {table} WHERE id = '{id}'
"""

# Универсальный запрос на изменение записи в таблице по id записи
edit_query = """
    UPDATE {table} SET {filed}={value} WHERE id='{}'
"""

# Запрос на добавление записи в таблицу
insert_query = """
    INSERT INTO {table}
    ({fileds}) VALUES ({values})
"""


### ФУНКЦИИ РАБОТЫ С БД ###

def connect():
    user = 'root'
    password = 'Turgenev1'
    host = 'localhost'
    db = 'nyam_pes'

    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def execute(query):
    connection = connect()
    result = ''
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
    finally:
        connection.close()
    return result