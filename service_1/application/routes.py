from application import app
from flask import Flask, request, render_template, url_for, redirect
from flask_mysqldb import MySQL
import requests
import random
import os

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    sentence = response.text
    return render_template('index.html', sentence = sentence, title = 'Home')

@app.route('/generatename', methods=['GET', 'POST'])
def home_create():
    if request.method == "POST":
        details=request.form
        UsersName=details['name']
        response = requests.get('http://service_4:5003/randomword')
        SuperNames = response.text
        cur = mysql.connection.cursor()
        cur.execute("INSERT IGNORE INTO SuperNames (UsersName, SuperNames) VALUES ((%s),(%s))", [UsersName, SuperNames])
        mysql.connection.commit()
        cur.close()
        return render_template('index.html', sentence = SuperNames, title = 'Home')