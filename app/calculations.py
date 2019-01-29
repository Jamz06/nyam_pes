from app.queries import simple_query, row_query, execute

TEST_DATA = {
    'dog_age': '2',
    'dog_weight': '7000',
    'dog_body_type': '1',
    'dog_breed': '1',
    'meat': '1',
    'sub_product': '2',
    'vegitables': '1',
    'poridge': '1'
}

MILKS = [
    {'Ингредиенты': 'Творог', 'Вес(грамм)':70, 'Цена':20 },
    {'Ингредиенты': 'Сметана', 'Вес(грамм)':70, 'Цена':12 },
    {'Ингредиенты': 'Яблоки', 'Вес(грамм)':50, 'Цена':6 },
    {'Ингредиенты': 'Бананы', 'Вес(грамм)':30, 'Цена':10 },
    {'Ингредиенты': 'Куриное яйцо', 'Вес(грамм)':50, 'Цена':6 },
    {'Ингредиенты': 'Итого:', 'Вес(грамм)':220, 'Цена':54 },

]


def calc_food_mass(age, weight):
    '''
        Функция расчета массы корма
    '''
    # age = percent from db
    # weight = gramm
    # Выбрать процент для расчета из БД
    percent = execute("select percent from age where id={}".format(age))
    percent = percent[0]['percent']

    result = (percent * int(weight))
    result = round(result,2)

    return result


def calc_food(data):
    """
        Функция расчета всего рациона
        Принимает словарь, с параметрами для расчета

        Возвращает:
            массив с ключами
            Ключи это поля таблицы
    """
    # Оснвной рацион
    # Вернет список словарей вида:
    # [ {
    #       'Продукт': 'Печень',
    #       'Вес': '100.0',
    #       'Цена': '100',
    #       'тип': 'мясо',
    # }, ...
    # ]
    primary_ration = []
    
    
    # Очистить словарь
    data = prepare_data(data)

    # dog_age = data.pop('dog_age')
    # dog_weight = data.pop('dog_weight')

    # Общий вес рациона
    ration_weight = calc_food_mass(data['dog_age'], data['dog_weight'])
    def get_product(id, weight, percent):
        '''
            Расчитать запись в таблице. вернуть название, вес, общую стоимость
        '''
        product = execute('select i.name "Продукт", t.name "Тип", i.price "Цена"  from ingredient i, ingredient_type t where i.type = t.id and i.id = {}'.format(id))
        product = product[0]

        product['Вес'] = weight / 100 * percent
        product['Цена'] = round(product['Цена'] * (product['Вес'] / 1000),2)

        return product

    if data['poridge'] != '':
        # # Расчитать цену       
        # Мясо
        primary_ration.append(get_product(data['meat'],ration_weight,30))
        # Субпродукты
        primary_ration.append(get_product(data['sub_product'], ration_weight, 30 ))
        # овощи
        primary_ration.append(get_product(data['vegitables'], ration_weight, 10 ))
        # Каша
        primary_ration.append(get_product(data['poridge'], ration_weight, 30 ))
    else:
        primary_ration.append(get_product(data['meat'],ration_weight,50))
        primary_ration.append(get_product(data['sub_product'],ration_weight,40))
        primary_ration.append(get_product(data['vegitables'],ration_weight,10))

    # Расчитать итог
    totals = {
        'Продукт': 'Итого:',
        'Тип': '',
        'Цена': 0,
        'Вес': 0
    }

    for row in primary_ration:
        totals['Цена'] += row['Цена']
        totals['Вес'] += row['Вес']

    primary_ration.append(totals)
    return primary_ration, ration_weight



def prepare_data(data):
    '''
        Очищает массив от ненужной ерунды
    '''
    # data.pop('dog_breed')
    # data.pop('dog_body_type')
    
    # print(data)

    return data


if __name__ == '__main__':
    ration, total_weigt = calc_food(TEST_DATA)
    print('Общий вес рациона {} грамм'.format(total_weigt))
    print('Рацион:')
    for r in ration:
        print(r)

