import sqlite3
import random
import os

print (os.getcwd())

conn = sqlite3.connect('SQLite_Python.db')
c = conn.cursor()


identificativo = 0
for n in range (10000):
	value = random.uniform(0.498, 0.503)
	identificativo = identificativo + 1
	x = (identificativo, value)
	try:
		c.execute('INSERT INTO table1 VALUES (?,?)', x)
		conn.commit()
		print('Insert succesful')
	except sqlite3.Error as e:
		print('An error occurred:' , e.args[0])
conn.close()
	
identificativo = 0
for n in range (10000):
	value = random.uniform(0.499, 0.501)
	identificativo = identificativo + 1
	x = (identificativo, value)
	try:
		c.execute('INSERT INTO table1 VALUES (?,?)', x)
		conn.commit()
		print('Insert succesful')
	except sqlite3.Error as e:
		print('An error occurred:' , e.args[0])
conn.close()		
