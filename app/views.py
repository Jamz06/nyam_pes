from flask import render_template, flash, redirect, request, abort, jsonify, send_from_directory, url_for, jsonify
from app import app
from app.forms import DogForm
from app.calculations import calc_food


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    """
        Главная страница с предложением заказа

    """
    # Форма с параметрами собаки
    dog_form = DogForm()
    print(dog_form.dog_age)
    if dog_form.validate_on_submit():
        print(request.form)
        flash('Форма подтверждена')
        # Расчитать всю фигню
        # Показать шаблон с размеченной таблицей
        data = dog_form.data
        print(data)
    return render_template(
        'index.html',
        form=dog_form,
        title="НямПес"
    )





@app.route('/static/<path:path>')
# Статику отдаем без авторизации
# @login_required
def send_js(path):
    # Отладочный вывод с информацией о запросе файла
    # flash("path is: " + path)
    return send_from_directory('static', path)


