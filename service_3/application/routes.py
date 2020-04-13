from application import app
import random


@app.route('/randomphrase', methods=['GET', 'POST'])
def ending():

	list = ['Woman', 'Man', 'Fist', 'Hero', 'Legend', 'God', 'Saint']
	
	return list[random.randrange(6)]