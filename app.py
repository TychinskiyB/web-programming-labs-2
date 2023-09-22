from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route('/lab1/oak')
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


@app.route("/menu")
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

        <h1>web-сервер на flask</h1>
        <footer>
            &copy; Богдан Тычинский, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>

'''


@app.route("/lab1")
def lab1():

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


@app.route('/lab1/student')
def sudent():
    return'''
<!doctype html>
<html>
    <h1>Тычинский Богдан Владимирович</h1>
    <img src="''' + url_for('static', filename='ЛОГО НГТУ.jpeg') + '''">
</html>
'''

@app.route("/lab1/qwer")
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
@app.route ('/lab2/example')
def example():
    return render_template('example.html')