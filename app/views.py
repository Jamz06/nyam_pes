from flask import render_template, flash, redirect, request, abort, jsonify, send_from_directory, url_for, jsonify
from app import app
from app.forms import DogForm
from app.calculations import calc_food
from app.queries import execute, edit_query, insert_query, row_query, simple_query, execute, tables_query, table_fields, delete_query, get_choices




@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    """
        Главная страница с предложением заказа

    """
    
    # Форма с параметрами собаки
    dog_form = DogForm()
    
    choices = get_choices()
    
    # Добавить выборы в поля
    dog_form.dog_age.choices = choices['age']
    dog_form.dog_body_type.choices = choices['body_type']
    dog_form.dog_breed.choices = choices['breed']
    dog_form.meat.choices = choices['meat']
    dog_form.sub_product.choices = choices['sub_product']
    dog_form.vegitables.choices = choices['vegitables']
    dog_form.poridge.choices = choices['poridge']

    data = {}
    if request.method == 'POST':
    # if dog_form.validate_on_submit():
        flash('Форма подтверждена')
        # Расчитать всю фигню
        data = request.form.to_dict()
        del data['csrf_token']
        del data['submit']
        print(data)
        
        # Показать шаблон с размеченной таблицей
        
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


