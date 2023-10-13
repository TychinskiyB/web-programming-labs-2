@app.route("/")
def qwer():
    return '''

<!doctype html>
<html>
    <head>
         
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='11111.css') + '''">
        <title>Тычинский Богдан Владимирович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <p>Жили гуси у бабуси</p>
        <h1>web-сервер на flask</h1>
        <footer>
            &copy; Богдан Тычинский, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>

'''


