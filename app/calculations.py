TEST_DATA = {'dog_age': '1', 'dog_weight': '5000', 'dog_body_type': '1', 'dog_breed': '1', 'meat': '1', 'sub_product': '7', 'vegitables': '3', 'poridge': '4'}

def calc_food_mass(age, weight):
    '''
        Функция расчета массы корма
    '''
    # age = percent from db
    # weight = gramm

    result = (age * weight) / 10

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
    primary_ration = []

    
    # Очистить словарь
    data = prepare_data(data)

    dog_age = data.pop('dog_age')
    dog_weight = data.pop('dog_weight')

    # Общий вес рациона
    ration_weight = calc_food_mass(dog_age, dog_weight)

    if data['porrige']:
        primary_ration.append(
            (data['meat'], ration_weight / 100 * 30),
            (data['sub_product'], ration_weight / 100 * 30),
            (data['vegitables'], ration_weight / 100 * 10),
            (data['poridge'], ration_weight / 100 * 30),
        )
    else:
        primary_ration.append(
            (data['meat'], ration_weight / 100 * 50),
            (data['sub_product'], ration_weight / 100 * 40),
            (data['vegitables'], ration_weight / 100 * 10),
        )

    return primary_ration



def prepare_data(data):
    '''
        Очищает массив от ненужной ерунды
    '''
    data.pop('dog_breed')
    data.pop('dog_body_type')
    data.pop('csrf_token')
    data.pop('submit')
    # print(data)

    return data


if __name__ == '__main__':
    foo = calc_food(TEST_DATA)
