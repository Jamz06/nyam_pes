# Активирует предотвращение поддельных межсайтовых запросов.
CSRF_ENABLED = False
# Используется для создания криптографического токена, который используется при валидации формы
SECRET_KEY = 'ReuLZLG95j8d4Dr78d9e2n,3bIUTas'


## MAIL
# От кого отправлять
# MAYBE: Стоит запихать настройки сервера почты в БД?
MAIL = {
    'from': 'nyam_pes@gmail.com', # Обратный адрес. (Может совпадать с логином)
    'server': 'smtp.gmail.com', # Адрес сервера
    'port': 465, # Порт
    'login': 'nyam_pes@gmail.com', # логин почты
    'password': 'ПАРОЛЬ СЮДА НАПИСАТЬ' # Пароль
}

### DB config ###
DB_CONF = {
    'user':'root',
    'password':'Turgenev1',
    'host':'localhost',
    'db':'nyam_pes'
}
 


