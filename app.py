from flask import Flask, request, jsonify, redirect, render_template

import sqlite3
import os

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    else:
        mail = request.form.get('mail')
        password = request.form.get('password')

        return jsonify({'mail': mail, 'password': password})

if __name__ == '__main__':
    app.run()