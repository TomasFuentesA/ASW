from flask import Flask, request, jsonify, redirect, render_template
from service_login import service_login

from cambiar_contrasena import *
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
            if log[1][6] == False:
                return render_template('cambio_contraseña.html', mail=mail)
            else:       
                return jsonify(log[1])

@app.route('/cambio_pw', methods=['POST'])
def cambio_contrasena():
    mail = request.form.get('mail')
    password = request.form.get('password')
    c_password = request.form.get('c_password')
    if password == c_password:
        log = service_cambio_contrasena(mail,password)

        return render_template('menu.html')
    else:
        return render_template('cambio_contraseña.html', value='Contraseña no coinciden')    


if __name__ == '__main__':
    time.sleep(25)