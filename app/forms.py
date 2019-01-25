from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.fields.html5 import DateField 
from wtforms.validators import DataRequired, Length


class DogForm(FlaskForm):
    """
        Основная форма сбора вопросов по собаке
    """

    # Возраст собаки
    dog_age = SelectField(
        label='Возраст собаки',
        choices = [
            ('1','1-5 месяцев'),
            ('2','6-12 месяцев'),
            ('3','1-3 года'),
            ('4','4-7 лет'),
        ],
    )
    # Вес собаки
    dog_weight = SelectField(
        label='Вес собаки',
        choices = [
            ('1','1-3 кг'),
            ('2','4-6 кг'),
            ('3', '7-10 кг'),
            ('4','11 кг и выше'),
        ],
    )

    # Телосложение собаки
    dog_body_type = SelectField(
        label='Телосложение собаки',
        choices = [
            ('1','Очень маленькая'),
            ('2','Маленькая'),
            ('3','Средняя'),
            ('4', 'Большая'),
            
        ],
    )

    # Тип породы
    dog_breed = SelectField(
        label='Тип породы собаки',
        choices = [
            ('1','Терьер'),
            ('2','Пастушья'),
            ('3', 'Гончая'),
            ('4','Ретривер, спаниель, водолаз'),
            ('5','Борзая'),
            ('6','Легавая'),
            ('7','Такса'),
            ('8','Пинчер, Шнауцер'),
            ('9','Шпицы'),
        ],
    )


    # Мясо
    meat = SelectField(
        label='Мясо',
        choices = [
            ('1','Мясо1'),
            ('2','Мясо2'),
            ('3','Мясо3'),
            ('4','Еще мясо'),
        ],
    )

    # Субпродукты
    sub_product = SelectField(
        label='Субпродукты',
        choices = [
            ('1','Почки'),
            ('2','Рубец'),
            ('3','Сердце'),
            ('4','Трахея'),
        ],
    )

    # Овощи
    vegitables = SelectField(
        label='Овощи',
        choices = [
            ('1','Овощ'),
            ('2','Еще овощ'),
            ('3','Ахуеть какой овощь'),
            ('4','Овощ2'),
        ],
    )



    # Крупа
    poridge = SelectField(
        label='Крупы',
        choices = [
            ('0','Ничего'),
            ('1','Крупа'),
            ('2','просто крупа'),
            ('3','Не просто крупа'),
            ('4','Дорогая крупа'),
        ],
    )

    # # Включить кисломолочку
    dog_inlude_milk = BooleanField(
        label='Включить Кисломолочные продукты'
    )

    submit = SubmitField('Расчитать')


class BaseEditForm(FlaskForm):
    """
        Шаблон для автособираемой формы редактирования/добавления поля таблицы
    """
    pass
    
    