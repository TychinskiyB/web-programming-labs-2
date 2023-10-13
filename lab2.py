from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)


@lab2.route ('/lab2/example')
def example():
    name, lab_num, group, course = 'Тычинский Богдан', 2, 'ФБИ-12', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html',
                            name=name, lab_num=lab_num, group=group,course=course, fruits=fruits )


@lab2.route ('/lab2/')
def laba():
    return render_template('lab2.html')
    