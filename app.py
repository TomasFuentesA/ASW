from flask import Flask, request, jsonify, redirect
import sqlite3
import os

DATABASE_NAME = 'IoT.db'

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("http://www.example.com", code=302)

if __name__ == '__main__':
    app.run()