from flask import Flask, redirect, url_for, render_template
<<<<<<< HEAD
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
=======
from lab1 import lab1 
from lab2 import lab2 
from lab3 import lab3 
from lab4 import lab4 
from lab5 import lab5 
>>>>>>> cfede355a62b2d6b135535a8f2fc079bb44b4fc1

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
<<<<<<< HEAD
app.register_blueprint(lab3)
=======
>>>>>>> cfede355a62b2d6b135535a8f2fc079bb44b4fc1
app.register_blueprint(lab4)
app.register_blueprint(lab5)