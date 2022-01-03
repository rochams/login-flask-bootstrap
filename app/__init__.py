from flask import Flask


app = Flask(__name__)

from app.models import form
from app.controllers import default


SECRET_KEY = 'uma-chave-segura'
app.config['SECRET_KEY'] = SECRET_KEY

DEBUG = True