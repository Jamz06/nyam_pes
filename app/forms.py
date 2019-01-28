from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
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
        validators=[DataRequired(message='Обязательное поле')],
    )
    # Вес собаки
    dog_weight = StringField(
        label='Вес собаки, В граммах',description="напишите в граммах",
        validators=[DataRequired(message='Обязательное поле')]
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
        validators=[DataRequired(message='Обязательное поле')],
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
        validators=[DataRequired(message='Обязательное поле')],
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
        validators=[DataRequired(message='Обязательное поле')],
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
        validators=[DataRequired(message='Обязательное поле')],
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
        validators=[DataRequired(message='Обязательное поле')],
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
    dog_include_milk = BooleanField(
        label='Включить Кисломолочные продукты'
    )

    submit = SubmitField('Расчитать')


class EditForm(FlaskForm):
    """
        Шаблон для автособираемой формы редактирования/добавления поля таблицы
    """

class ContactForm(FlaskForm):
    """
        Форма обратной связи
    """
    name = StringField(label='Как к Вам обращаться?', description='Напрмер: Борис',validators=[DataRequired(message='Обязательное поле')])
    phone = StringField(label='Телефон', description='8XXXXXXXXXX',)
    email = StringField(label='Электронная почта', description='example@gmail.com', validators=[DataRequired(message='Обязательное поле')])
    submit = SubmitField('Отправить')

if __name__ == '__main__':
    test_form = EditForm()
    
    