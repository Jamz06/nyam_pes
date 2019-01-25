from flask import render_template, flash, redirect, request, abort, jsonify, send_from_directory, url_for, jsonify
from app import app
from app.queries import execute, edit_query, insert_query, row_query, simple_query, execute, tables_query, table_fields
from flask import Markup
# from app.forms import EditForm

from app.form_constructor import construct_form

table_names = execute(tables_query)
print(table_names)
@app.route('/admin/')
@app.route('/admin/index')
def admin_index():
    return render_template('admin/index.html', tables=table_names)


@app.route('/admin/view/<string:table>')
def view_table(table):
    """
        Просмотр выбранной таблицы
    """
    query = simple_query.format(table=table)
    result = execute(query)
    print(result)
    return render_template('admin/view.html', result=result, table=table, tables=table_names)


@app.route('/admin/edit/<string:table>/<string:id>', methods=['GET', 'POST'])
def edit_table(table, id):
    """
        Изменить запись в таблице
    """
    
    
    # Получить запись из таблицы
    data = execute(
        row_query.format(
            table=table,
            id=id
        )
    )
    # Добавить поля в форму, на основе полей таблицы
    form_fields = execute(table_fields.format(table=table))
    form = construct_form(form_fields)
    print(form)
    
    
    
    # Валидация формы
    # TODO: Добавить валидацию!
    


    return render_template('admin/edit_add.html', tables=table_names, form=Markup(form), data=data)


@app.route('/admin/add/<string:table>', methods=['GET', 'POST'])
def add_row(table):
    """
        Добавить запись в таблицу
    """
    form = EditForm()
    
    form_fields = execute(table_fields.format(table=table))
    # Получить запись из таблицы
    
    # Добавить поля в форму, на основе полей таблицы
    form = construct(form, form_fields)
    new_form = form
    print(new_form.age)
    
    # Валидация формы
    # TODO: Добавить валидацию!
    return render_template('admin/edit_add.html', tables=table_names, form=new_form)




