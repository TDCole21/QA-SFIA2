import pytest
import urllib3
from flask import Flask, render_template, request
import os
from flask_mysqldb import MySQL
import requests
import csv

app = Flask(__name__)

# app.config['MYSQL_HOST']=os.environ['MYSQL_HOST']
# app.config['MYSQL_USER']=os.environ['MYSQL_USER']
# app.config['MYSQL_PASSWORD']=os.environ['MYSQL_PASSWORD']
# app.config['MYSQL_DB']=os.environ['MYSQL_DB']

mysql = MySQL(app)

url = "http://35.246.71.197/"
url2 = "http://35.189.90.40/"

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

def test_ports_1_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', url+"/80")
    assert 500 == r.status

def test_ports_1_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', url2+"/80")
    assert 500 == r.status

def test_ports_2_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', url+"/5000")
    assert 500 == r.status

def test_ports_2_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', url2+"/5000")
    assert 500 == r.status

def test_ports_3_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', url+"/5001")
    assert 500 == r.status

def test_ports_3_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', url2+"/5001")
    assert 500 == r.status

def test_ports_4_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', url+"/5002")
    assert 500 == r.status

def test_ports_4_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', url2+"/5002")
    assert 500 == r.status

def test_ports_5_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', url+"/5003")
    assert 500 == r.status

def test_ports_5_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', url2+"/5003")
    assert 500 == r.status

def test_ports_6_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', url+"/5004")
    assert 500 == r.status

def test_ports_6_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', url2+"/5004")
    assert 500 == r.status
