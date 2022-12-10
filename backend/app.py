from flask import Flask, request, jsonify, redirect, render_template
from service_login import service_login

import os
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    else:
        mail = request.form.get('mail')
        password = request.form.get('password')
        log = service_login(mail, password)
        if not log[0]:
            return []
        if (log[0] and log[1] == None):
            return []
        else:
            if log[1][6] == 0:
                return render_template('cambio_contraseña.html')
            else:       
                return render_template('menu.html')


if __name__ == '__main__':
    time.sleep(25)