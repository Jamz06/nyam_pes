from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, IntegerField, DateTimeField, SubmitField
from wtforms.fields.html5 import DateField 
from wtforms.validators import DataRequired, Length
from wtforms_dynamic_fields import WTFormsDynamicFields
from app.forms import EditForm

def construct(object, form_fields):
    """
        Функция фабрика.
        Собирает форму по указанным параметрам
        Принимает:
            oject: Экземпляр класса формы
            form_fields(list[dicts]): Параметры формы. Список словарей
        Возвращает:
            Экземпляр класса формы
    """
    # Обойти список, добавить к экземпляру класса новые параметры
    # В свойства поля попадают следующие параметры
    # COLUMN_COMMENT, COLUMN_NAME, COLUMN_KEY, COLUMN_TYPE, IS_NULLABLE

    # Временная переменная для присвоения атрибутов поля формы
    # temp_field = None
    dynamic = WTFormsDynamicFields()

    for field in form_fields:
        label = field['COLUMN_COMMENT']

        # Если поле даты
        if field['COLUMN_TYPE'] == 'datetime':
            dynamic.add_field(field['COLUMN_NAME'], label, DateTimeField)
            # temp_field = DateTimeField(label=label)

        # Если поле числовое
        elif 'int' in field['COLUMN_TYPE']:
            dynamic.add_field(field['COLUMN_NAME'], label, IntegerField)
            # temp_field = IntegerField(label=label)

        # Все остальные просто текст пусть будут
        else:
            dynamic.add_field(field['COLUMN_NAME'], label, StringField)
            # temp_field = StringField(label=label)

        if field['IS_NULLABLE'] == 'YES':
            dynamic.add_validator(field['COLUMN_NAME'], DataRequired, message='Обязательное поле')
            # temp_field.validators=DataRequired()

        # Присвоить экземпляру класса новый атрибут
        # setattr(object, field['COLUMN_NAME'], temp_field)

        # object.__setitem__(field['COLUMN_NAME'], temp_field)
        
    object = dynamic.process(EditForm)
    # object.__setitem__('submit', SubmitField('Сохранить'))
    # setattr(object, 'submit', SubmitField('Сохранить'))


    return object


