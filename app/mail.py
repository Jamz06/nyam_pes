# Модуль отправки почты

import smtplib
from config import MAIL
from email.mime.text import MIMEText

def send_mail(to=[], message='Test message', subject='Test message'):
    """
        Функция отправки почты.
        Принимает:
            - to:Список адресов для отправки
            - message: Текст письма
            - subject: Тема письма
    """
    # От кого отправлять
    me = MAIL['from']
    # Преобразовать текст в MIME для отправкик
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = me
    for t in to:
        msg['To'] = t
        s = smtplib.SMTP(MAIL['server'], MAIL['port'])
        s.ehlo()
        s.login(MAIL['login'], MAIL['password'])
        s.sendmail(me, t, msg.as_string())

    s.quit()


if __name__ == '__main__':
    send_mail(to=['e.vysotin@cocos.perm.ru'])