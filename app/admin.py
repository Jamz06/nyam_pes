from flask import render_template, flash, redirect, request, abort, jsonify, send_from_directory, url_for, jsonify
from app import app
from app.queries import execute, edit_query, insert_query, row_query, simple_query, execute


@app.route('/admin/view/<string:table>')
def view_table(table):
    """
        Просмотр выбранной таблицы
    """
    query = simple_query.format(table=table)
    result = execute(query)
    print(result)
    return render_template('admin/view.html', result=result, table=table)


@app.route('/admin/edit/<string:table>')
def edit_table(table):
    """
        Изменить запись в таблице
    """

    return render_template('admin/edit.html')


@app.route('/admin/add/<string:table>')
def add_row(table):
    """
        Добавить запись в таблицу
    """

    return render_template('admin/add.html')




