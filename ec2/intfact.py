#!/usr/bin/python3

import sys
from flask import *

def factorize(num):
    num = str(num)
    return num

app = Flask(__name__)

@app.route('/')
def index():
    return "Usage: /num/<number to be factored>"

@app.get('/num/<number>')
def _factorize_get_(number):
    num = str(number)
    return factorize(num)

@app.post('/num')
def _factorize_post_():
    num = str(request.form['number'])
    return factorize(num)
