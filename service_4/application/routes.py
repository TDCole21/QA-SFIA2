from application import app
import requests

@app.route('/randomword', methods=['GET', 'POST'])
def sentence():
    beginning = requests.get('http://service_2:5001/randomphrase')
    ending = requests.get('http://service_3:5002/randomphrase')
    response = beginning.text + " " + ending.text
    return response

@app.route('/randomword/hero', methods=['GET', 'POST'])
def sentence_hero():
    beginning = requests.get('http://service_2:5001/randomphrase/hero')
    ending = requests.get('http://service_3:5002/randomphrase/hero')
    response_hero = beginning.text + " " + ending.text
    return response_hero

@app.route('/randomword/villain', methods=['GET', 'POST'])
def sentence_villain():
    beginning = requests.get('http://service_2:5001/randomphrase/villain')
    ending = requests.get('http://service_3:5002/randomphrase/villain')
    response_villain = beginning.text + " " + ending.text
    return response_villain