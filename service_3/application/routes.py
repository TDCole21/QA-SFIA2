from application import app
import random


@app.route('/randomphrase', methods=['GET', 'POST'])
def ending():

	list = ['Woman', 'Man', 'Fist', 'Hero', 'Legend', 'God', 'Saint']
	
	return list[random.randrange(6)]

@app.route('/randomphrase/hero', methods=['GET', 'POST'])
def ending_hero():

	list = ['Woman', 'Man', 'Fist', 'Hero', 'Legend', 'God', 'Saint']
	
	return list[random.randrange(6)]

@app.route('/randomphrase/villain', methods=['GET', 'POST'])
def ending_villain():

	list = ['Woman', 'Man', 'Fist', 'Hero', 'Legend', 'God', 'Saint']
	
	return list[random.randrange(6)]