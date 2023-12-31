from flask import Blueprint, redirect, url_for, render_template
lab1 = Blueprint('lab1',__name__)

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route('/lab1/oak')
def oak():
    return'''

<!doctype html>
<html>
    <head>
         <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Тычинский Богдан Владимирович, лабораторная 1</title>
    </head>
    <body>
        <h1>Дуб</h1>
    
        <img src="'''+ url_for('static', filename='Дуб.jpg',) + '''">
      
    </body>
</html>
'''


@lab1.route("/menu")
def menu():
    return '''

<!doctype html>
<html>
    <head>
         <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Тычинский Богдан Владимирович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
    <main>
                <li>
                    <a href="/lab1" target="_blank">Лабораторная работа №1</a>
                </li>
                <li>
                    <a href="/lab2" target="_blank">Лабораторная работа №2</a>
                </li>
                <li>
                    <a href="/lab3" target="_blank">Лабораторная работа №3</a>
                </li>
                <li>
                    <a href="/lab4" target="_blank">Лабораторная работа №4</a>
                </li>
    </main>
        <h1>web-сервер на flask</h1>
        <footer>
            &copy; Богдан Тычинский, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>

'''


@lab1.route("/lab1/")
def lab():
    return '''


<!doctype html>
<html>
    <head>
     <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Тычинский Богдан Владимирович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
Flask — фреймворк для создания веб-приложений на языке
программирования Python, использующий набор инструментов
Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
называемых микрофреймворков — минималистичных каркасов
веб-приложений, сознательно предоставляющих лишь самые ба-
зовые возможности.
        <h1>web-сервер на flask</h1>
         <a href="/menu" target="_blank">меню</a>
         <main>
            <ul>
                <li>
                    <a href="http://127.0.0.1:5000/lab1/oak" target="_blank">Дуб</a>
                </li>
            </ul>
            <ul>
                <li>
                    <a href="http://127.0.0.1:5000/lab1/student" target="_blank">Студент</a>
                </li>
            </ul>
            <ul>
                <li>
                    <a href="http://127.0.0.1:5000/lab1/python" target="_blank">Python</a>
                </li>
            </ul>
            <ul>
                <li>
        </main
        <footer>
            &copy; Богдан Тычинский, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route('/lab1/student')
def sudent():
    return'''
<!doctype html>
<html>
    <h1>Тычинский Богдан Владимирович</h1>
    <img src="''' + url_for('static', filename='ЛОГО НГТУ.jpeg') + '''">
</html>
'''


@lab1.route("/lab1/qwer")
def qwer():
    return '''

<!doctype html>
<html>
    <head>
         
        # <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Тычинский Богдан Владимирович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <p class="rer">Жили гуси у бабуси</p>
        <h1>web-сервер на flask</h1>
        <footer>
            &copy; Богдан Тычинский, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>

'''
