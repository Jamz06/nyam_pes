from flask import render_template, flash, redirect, request, abort, jsonify, send_from_directory, url_for, jsonify
from app import app
from app.forms import DogForm, ContactForm
from app.calculations import calc_food, MILKS
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
        #  flash('Форма подтверждена')
        # Расчитать всю фигню
        data = request.form.to_dict()
        del data['csrf_token']
        del data['submit']
        print(data)
        # Костыль:  сколько раз кормить
        feed = execute('select age, feed from age where id={}'.format(data['dog_age']))
        # Поместить в массив нужные данные

        ration, total_weigt = calc_food(data)
        print('Общий вес рациона {} грамм'.format(total_weigt))
        print(ration)
        # Кисломолочка
        try:
            if data['dog_include_milk']:
                milks = MILKS
        except Exception:
            milks = None
        
        # Добавить форму обратной связи
        contact_form = ContactForm()
        # Показать шаблон с размеченной таблицей
        # 
       
        return(render_template('order.html', result=ration, weight=total_weigt, milks=milks, contact_form=contact_form, feed=feed[0]))
        
        
    return render_template(
        'index.html',
        form=dog_form,
        title="НямПес"
    )


@app.route('/order', methods=['POST'])
def order():
    if not request.json:
        abort(400)
    
    params = request.json
    # print('JSON has come! Here it is:  ')
    # print(params)
    customer = params['customer']
    products = params['order_data']
    
    # Проверить на существующий email
    customer_id = execute("select id from customer where email = '{}'".format(customer['email']))
    if not customer_id:
        print(customer_id)
        data_to_update = ''
        # print(customer)

        data_to_update += "name = '{name}', email = '{email}', phone='{phone}' ".format(
            name=customer['name'],
            email=customer['email'],
            phone=customer['phone']
        )
        
        # debug Вывести запрос в БД
        query = insert_query.format(
                table='customer',
                setter=data_to_update,
            )
        # Выполнить обновление записи
        print(query)
        execute(query)

        customer_id = execute("select id from customer last")
        customer_id = customer_id[0]




    return '200'

@app.route('/buy')
def buy():
    return redirect(url_for('index'))

@app.route('/static/<path:path>')
# Статику отдаем без авторизации
# @login_required
def send_js(path):
    # Отладочный вывод с информацией о запросе файла
    # flash("path is: " + path)
    return send_from_directory('static', path)


