# Модуль с запросами

import pymysql.cursors

from config import DB_CONF

# Универсальный Запрос под нужную таблицу. Выбрать все записи.
simple_query = """
    SELECT * FROM {table} order by id
"""

# Универсальный запрос под нужную таблицу. Выбрать запись по ID
row_query = """
    SELECT * FROM {table} WHERE id = '{id}'
"""

# Универсальный запрос на изменение записи в таблице по id записи
edit_query = """
    UPDATE {table} SET {setter} WHERE id='{id}'
"""

# Запрос на добавление записи в таблицу
insert_query = """
    INSERT INTO {table}
    SET {setter}
"""

insert_query_classic = """
    INSERT INTO {table}
    ({fileds}) VALUES ({values})
"""

delete_query = """
    DELETE 
    FROM {table}
    WHERE id = '{id}'
"""

# Запрос на выбор имен всех таблиц БД, для обращения к ним и создания ссылок на их просмотр
tables_query = """
    SELECT TABLE_NAME, TABLE_COMMENT FROM INFORMATION_SCHEMA.TABLES where table_schema='{db_name}'
""".format(db_name=DB_CONF['db'])

table_fields = """
    SELECT COLUMN_COMMENT, COLUMN_NAME, COLUMN_KEY, COLUMN_TYPE, IS_NULLABLE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE
    table_name = '{table}'
    and column_key != 'PRI'
"""

### ФУНКЦИИ РАБОТЫ С БД ###

def connect():
    user = DB_CONF['user']
    password = DB_CONF['password']
    host = DB_CONF['host']
    db = DB_CONF['db']

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
        connection.commit()
        connection.close()
    return result