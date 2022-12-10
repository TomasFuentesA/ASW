from flask import Flask, request, jsonify, redirect, render_template
from backend.service_login import service_login

import sqlite3
import os

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
        if (service_login(mail, password)):
            return jsonify({'mail': mail, 'password': password})
        else:
            return 0
