from os import MFD_HUGE_SHIFT
from app import app
from flask import render_template

from app.models.form import LoginForm

# o ROUTE define o que será executado no caminho especificado.

@app.route('/')         # Criando caminho para a RAIZ
def raiz():
    return '<h2>Para entrar: "<u>127.0.0.1:5000/login"</u></h2><br><h2>Para acessar seu perfil: "<u>127.0.0.1:5000/seu_nome"</u>'


@app.route('/index/<user>')
@app.route('/index', defaults={"user":None})
def user(user):
    return render_template('index.html', user=user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)       # Prints feitos no terminal
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route('/base')
def base():
    return render_template('base.html')

