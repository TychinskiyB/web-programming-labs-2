from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')



@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')

    if drink == 'cofee':
        price == 120 
    elif drink == 'black-tea':
        price == 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price = price)

@lab3.route('/lab3/succces')
def succces():
    return render_template('succes.html')

@lab3.route('/lab3/zach')
def zach():
    
    A = request.args.get("A")
    B = request.args.get("B")
    C = request.args.get("C")
    D = request.args.get("D")

    if A and B and C and D:
            
        A = float(A)
        B = float(B)
        C = float(C)
        D = float(D)
    if A==B==C:
        result = 4
    elif A==B==D:
        result = 3
    elif A==C==D:
        result = 2
    else:
        result = 1


    return render_template('zachita1 laba.html', result = result, A = A, B = B, C = C, D = D)




@lab3.route('/lab3/zac3')
def zac3():
    n=6
    k=2
    sum=0
    for i in range(1,n+1):
        sum=sum+i**k
    return f"sum={sum}"


