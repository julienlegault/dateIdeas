const sqlite3 = require('sqlite3').verbose();

var sql;
var isFoodBox = true;
var isNotFoodBox = true;
var isOutsideBox = true;
var isNotOutsideBox = true;
var currentLat = 41.632795;
var currentLon = -70.605235;
var minPriceIn = 0; 
var maxPriceIn = 100;
var radius = 10000;

function getFoodBox(){
	return isFoodBox;
}

function getNotFood(){
	return isNotFoodBox;
}

function getOutsideBox(){
	return isOutsideBox;
}

function getNotOutside(){
	return isNotOutsideBox;
}

function getMinPrice(){
	return minPriceIn;
}

function getMaxPrice(){
	return maxPriceIn;
}

function getRadius(){
	return radius;
}

function getLocation(){
}

function distanceBetween(lat1, lon1, lat2, lon2) {
	var earthRadius = 6371;
	var dLat = degreesToRadians(lat2-lat1);
	var dLon = degreesToRadians(lon2-lon1);
	lat1 = degreesToRadians(lat1);
	lat2 = degreesToRadians(lat2);
	var a = Math.sin(dLat/2) * Math.sin(dLat/2) + Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2);
	var c = 2* Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
	return earthRadius * c * 0.621371;
}

function degreesToRadians(degrees) {
	return degrees * Math.PI / 180;
}

function inRange(locId){
	let db = new sqlite3.Database('./dateDatabase.db');
	sql = 'SELECT lat, lon FROM locations WHERE id=' + locId;
	db.all(sql, [], (err, rows) => {
		if(err){
			throw err;
		}
		rows.forEach(function(row) {
			var distance = distanceBetween(currentLat, currentLon, row.lat, row.lon);
			if(distance <= getRadius()){
				return true;
			}
			else {
				return false;
			}
		});
	});
}

function getRandomDate(){
	let db = new sqlite3.Database('./dateDatabase.db');
	var locationArray = [];
	sql = 'SELECT * FROM locations';
	db.all(sql, [], (err, rows) => {
		if(err){
			throw err;
		}
		rows.forEach(function(row) {
			console.log(inRange(row.id));
			if(inRange(row.id)){
				console.log(row);
				locationArray.push(row);
			}
		});
	});
	locationArray.forEach(function(id){
		sql = 'SELECT d.*, l.* FROM dates AS d INNER JOIN d2l r ON r.dateId = d.id INNER JOIN locations l ON l.id = r.locId WHERE l =' + id;
		db.all(sql, [], (err, rows) => {
			if(err){
				throw err;
			}
			rows.choose(function(row) {
				console.log(row);
			});
		});
	});

	db.close();
}

function getManualLocation(){

}

function addDate(){

}

function addLoc(){

}

function linkD2L(){

}

function updateRecords(){

}


getRandomDate();
