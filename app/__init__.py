import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


# Подключить конфиг
app.config.from_object('config')


if not os.path.exists('logs'):
    os.mkdir('logs')
logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('logs/access.log')
logger.addHandler(handler)

file_handler = RotatingFileHandler('logs/web.log',maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.setLevel(logging.DEBUG)

app.logger.addHandler(file_handler)
app.logger.info('Старт лога')


from app import views, errors
