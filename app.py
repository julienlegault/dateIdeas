from flask import Flask, render_template, request
from constants import IpConstants, MapsConstants
import sqlite3
import random

app = Flask(__name__)

currentLoc = [0, 0]

def getRandomLocation(dateId):
	conn=sqlite3.connect('dateDatabase.db')
	curs=conn.cursor()
	resultList = []
	result = []
	for row in curs.execute("SELECT l.lat, l.lon FROM dates d INNER JOIN d2l r on r.dateId = d.id INNER JOIN locations l on l.id = r.locId where d.id = " + str(dateId)):
		resultList.append(row)
	try:
		result = random.choice(resultList)
	except:
		return [0,0]
	conn.close()
	return result

def getMap(dateName, locArray):
	if(locArray[0] == 0 and locArray[1] == 0):
		return MapsConstants.ERRORIMAGE 
	mapString = "https://maps.googleapis.com/maps/api/staticmap?size=400x400"
	apiKey = MapsConstants.KEY
	marker = "&markers=color:blue%7C" + str(locArray[0]) + "," + str(locArray[1])
	result = mapString + marker + apiKey
	return result

def getRandomDate(isFood, isNotFood, isOutside, isNotOutside, distance, minPrice, maxPrice):
	conn=sqlite3.connect('dateDatabase.db')
	curs=conn.cursor()
	sql = "SELECT * FROM dates WHERE (price > " + str(minPrice) + " AND price < " + str(maxPrice) + ") "
	if(isFood == 'True' and not isNotFood == 'True'):
		sql += " AND isFood = 1"
	elif(isNotFood == 'True' and not isFood == 'True'):
		sql += " AND isFood = 0"
	if(isOutside == 'True' and not isNotOutside == 'True'):
		sql += " AND isOutside = 1"
	elif(isNotOutside == 'True' and not isOutside == 'True'):
		sql += " AND isOutside = 0"
	resultList = []
	print(sql)
	for row in curs.execute(sql):
		resultList.append(row)
	result = random.choice(resultList)
	conn.close()
	return result

@app.route('/')
def index():
	templateData = {
		'ResultVisible' : 'hidden',
		'currentPos' : currentLoc
		
	}
	return render_template('index.html', **templateData)

@app.route('/', methods=['POST', 'GET'])
def formSubmit():
	date = [0, 0, 0, 0, 0]
	if request.method == 'POST':
		isFood = request.form.get('isFood')
		isNotFood = request.form.get('isNotFood')
		isOutside = request.form.get('isOutside')
		isNotOutside = request.form.get('isNotOutside')
		distance = request.form.get('distance')
		minPrice = int(request.form.get('minPrice'))
		maxPrice = int(request.form.get('maxPrice'))
		date = getRandomDate(isFood, isNotFood, isOutside, isNotOutside, distance, minPrice, maxPrice)
	templateData = {
		'ResultVisible' : 'visable',
		'DateName' : date[1],
		'DatePrice' : '$' + "{:12.2f}".format(date[2]),
		'DateDescription' : 'Is food' if date[3] else 'Is not food',
		'LocationName' : 'Is outside' if date[4] else 'Is not outside',
		'GoogleMap': getMap(date[1], getRandomLocation(date[0]))
	}
	return render_template('index.html', **templateData)

@app.route('/api', methods=['POST'])
def getLocation():
	if request.method == 'POST':
		lat = request.form.get('lat')
		lon = request.form.get('lon')
		currentLoc = [lat, lon]

if __name__ == '__main__':
	app.run(debug=True, host=IpConstants.TESTING, port=IpConstants.TESTING_PORT)
