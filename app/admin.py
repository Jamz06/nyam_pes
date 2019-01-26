from flask import render_template, flash, redirect, request, abort, jsonify, send_from_directory, url_for, jsonify
from app import app
from app.queries import execute, edit_query, insert_query, row_query, simple_query, execute, tables_query, table_fields, delete_query

from app.forms import EditForm

from app.form_constructor import construct
# # 

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, IntegerField, DateTimeField, SubmitField
from wtforms.fields.html5 import DateField 
from wtforms.validators import DataRequired, Length
from wtforms_dynamic_fields import WTFormsDynamicFields
#####

table_names = execute(tables_query)
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
    form = EditForm()
    # Получить запись из таблицы
    data = execute(
        row_query.format(
            table=table,
            id=id
        )
    )

    
    # form_fields = execute(table_fields.format(table=table))
    # В какие поля вставлять
    
    data_to_update = ''
    if form.validate_on_submit():
        flash('Сохранено ;)')
        print(form)
        
        raw_data = request.form
        
        for row in raw_data:
            if row != 'csrf_token':
                # Строка для апдейта
                data_to_update += "{}='{}', ".format(row,raw_data[row])
        
        # debug Вывести запрос в БД
        query = edit_query.format(
                table=table,
                setter=data_to_update[0:-2],
                id=id
            )
        # Выполнить обновление записи
        execute(query)
        return redirect(url_for('view_table', table=table))
        

    return render_template('admin/edit_add.html',table=table, tables=table_names, data=data, form=form)


@app.route('/admin/add/<string:table>', methods=['GET', 'POST'])
def add_row(table):
    """
        Добавить запись в таблицу
    """
    
    form = EditForm()
    # Получить запись из таблицы
    data = execute(
        table_fields.format(
            table=table
        )
    )

    print(data)
    data_to_update = ''
    if form.validate_on_submit():
        flash('Добавлено ;)')
        print(form)
        
        raw_data = request.form
        
        for row in raw_data:
            if row != 'csrf_token':
                # Строка для апдейта
                data_to_update += "{}='{}', ".format(row,raw_data[row])
        
        # debug Вывести запрос в БД
        query = insert_query.format(
                table=table,
                setter=data_to_update[0:-2]
                
            )
        print(query)
        # Выполнить обновление записи
        execute(query)
        return redirect(url_for('view_table', table=table))
        

    return render_template('admin/add.html',table=table, tables=table_names, data=data, form=form)


@app.route('/admin/delete/<string:table>/<string:id>', methods=['GET', 'POST'])
def delete_row(table,id):

    execute(
        delete_query.format(
            table=table,
            id=id
        )
    )
    flash('Запись удалена')
    return redirect(url_for('view_table', table=table))
