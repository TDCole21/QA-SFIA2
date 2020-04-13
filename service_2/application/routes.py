from application import app
import random


@app.route('/randomphrase', methods=['GET', 'POST'])
def beginning():

	list = ['Super ','Bat ','Wonder ','The Amazing ','Dr. ', 'The Incredible ','Iron ']
	
	return list[random.randrange(6)]