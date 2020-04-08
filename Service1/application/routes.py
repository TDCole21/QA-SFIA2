from application import app
from flask import Flask, request, render_template, url_for, redirect
from flask_mysqldb import MySQL
import requests
import random
import os

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://service_4:5003/randomword')
    sentence = response.text
    return render_template('index.html', sentence = sentence, title = 'Home')