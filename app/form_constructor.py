# from flask_wtf import FlaskForm
# from wtforms import StringField, SelectField, FloatField, IntegerField, DateTimeField, SubmitField
# from wtforms.fields.html5 import DateField 
# from wtforms.validators import DataRequired, Length
# from wtforms_dynamic_fields import WTFormsDynamicFields
# from app.forms import EditForm


# def recreate_field(unbound):
#     """
#         Create new instance of the unbound field, resetting wtforms creation counter.

#         :param unbound:
#             UnboundField instance
#     """
#     if not isinstance(unbound, UnboundField):
#         raise ValueError('recreate_field expects UnboundField instance, %s was passed.' % type(unbound))

#     return unbound.field_class(*unbound.args, **unbound.kwargs)

# def construct(object, form_fields):
#     """
#         Функция фабрика.
#         Собирает форму по указанным параметрам
#         Принимает:
#             oject: Экземпляр класса формы
#             form_fields(list[dicts]): Параметры формы. Список словарей
#         Возвращает:
#             Экземпляр класса формы
#     """
#     # Обойти список, добавить к экземпляру класса новые параметры
#     # В свойства поля попадают следующие параметры
#     # COLUMN_COMMENT, COLUMN_NAME, COLUMN_KEY, COLUMN_TYPE, IS_NULLABLE

#     # Временная переменная для присвоения атрибутов поля формы
#     temp_field = None
#     dynamic = WTFormsDynamicFields()

#     for field in form_fields:
#         label = field['COLUMN_COMMENT']

#         # Если поле даты
#         if field['COLUMN_TYPE'] == 'datetime':
#             # dynamic.add_field(field['COLUMN_NAME'], label, DateTimeField)
#             temp_field = DateTimeField(label=label)

#         # Если поле числовое
#         elif 'int' in field['COLUMN_TYPE']:
#             # dynamic.add_field(field['COLUMN_NAME'], label, IntegerField)
#             temp_field = IntegerField(label=label)

#         # Все остальные просто текст пусть будут
#         else:
#             # dynamic.add_field(field['COLUMN_NAME'], label, StringField)
#             temp_field = StringField(label=label)

#         if field['IS_NULLABLE'] == 'NO':
#             # dynamic.add_validator(field['COLUMN_NAME'], DataRequired, message='Обязательное поле')
#             temp_field.validators=DataRequired()

#         # Присвоить экземпляру класса новый атрибут
#         setattr(object, field['COLUMN_NAME'], temp_field)
#         object.recreate_field()

#         # object.__setitem__(field['COLUMN_NAME'], temp_field)
        
#     # object = dynamic.process(EditForm, '')
#     # object.__setitem__('submit', SubmitField('Сохранить'))
#     setattr(object, 'submit', SubmitField('Сохранить'))



#     return object


label_field =  '<div class="input-group-addon">{label}</div>'
input_field = '<input id="{id}" type="{type}" {required} value="{value}">/'
element_div = '<div class="input-group mb-3">{input}</div>'
form_group = '<div class="form-group">{form_div}</div>'
submit = '<input class="btn btn-primary" type="submit" value="Сохранить" >'

def construct_form(fields):
    '''
        Конструктор HTML Форм
    '''
    field_set = []
    div = ''
    for field in fields:
        label = field['COLUMN_COMMENT']

        # Если поле даты
        if field['COLUMN_TYPE'] == 'datetime':
            f = input_field.format(
                    id=field['COLUMN_NAME'],
                    type='date',
                    value='',
                    required=''
                )
            

        # Если поле числовое
        else:
            f = input_field.format(
                    id=field['COLUMN_NAME'],
                    type='text',
                    value='',
                    required=''
                )
            
        if field['IS_NULLABLE'] == 'NO':
            f.format(required='required')
            
        field_set.append(
                label_field.format(label=label)
                + '\n'
                + f
            )
    
    for f in field_set:
        div += f + '\n'
    form = form_group.format(form_div=div)
    form += '\n' + submit      
    return form