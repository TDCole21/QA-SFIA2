from application import app
import random

@app.route('/randomphrase', methods=['GET', 'POST'])
def beginning():

	list = ['Super ','Bat ','Wonder ','The Amazing ','Dr. ', 'The Incredible ','Iron ']
	
	return list[random.randrange(6)]

@app.route('/randomphrase/hero', methods=['GET', 'POST'])
def beginning_hero():

	list = ['Super ','Bat ','Wonder ','The Amazing ','Dr. ', 'The Incredible ','Iron ']
	
	return list[random.randrange(6)]

@app.route('/randomphrase/villain', methods=['GET', 'POST'])
def beginning_villain():

	list = ['Dasterdly ','Evil ','Malicious ','The Destroyer of Worlds, ','Dr. ', 'The Villainous ','Dark ']
	
	return list[random.randrange(6)]