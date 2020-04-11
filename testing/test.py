import pytest
import urllib3
from flask import Flask, render_template, request
import os
from flask_mysqldb import MySQL
import requests
import csv

app = Flask(__name__)

app.config['MYSQL_HOST']=os.environ['MYSQL_HOST']
app.config['MYSQL_USER']=os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQL_DB']

mysql = MySQL(app)

url = "http://35.246.48.106/"
url2 = "http://34.89.110.7/"

def test_node_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    assert 200 == r.status

def test_node_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', url2)
    assert 200 == r.status

def test_getresponse():
    r = requests.get(url2)
    assert isinstance(r.text, str)

def test_getresponse2():
    r = requests.get(url)
    assert isinstance(r.text, str)

# def test_csv_service2():
#     for row in open("/home/Admin/projects/RapperNameGenerator/service_2/application/first.txt"):
#         coloumnlist = str(row)
#         coloumnlist = coloumnlist.split(",")
#     assert len(coloumnlist) == 25

# def test_csv_service3():
#     for row in open("/home/Admin/projects/RapperNameGenerator/service_3/application/last.txt"):
#         coloumnlist = str(row)
#         coloumnlist = coloumnlist.split(",")
#     assert len(coloumnlist) == 16

# def test_sql_insert():
#     with app.app_context():
#         cur = mysql.connection.cursor()
#         numRecordsOld = cur.execute("SELECT * FROM entries")
#         print(numRecordsOld)
#         cur.execute("INSERT INTO entries(name_old, name_new) VALUES ('Mark', 'Big Smoke');")
#         mysql.connection.commit()
#         numRecordsNew = cur.execute("SELECT * FROM entries")
#         print(numRecordsNew)
#         mysql.connection.commit()
#         cur.close()
#         assert numRecordsNew >= numRecordsOld