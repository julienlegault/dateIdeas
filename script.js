const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('./dateDatabase.db');
var i;
var sql;

for(i = 0; i < 58; i++){
	sql = 'SELECT l.name FROM dates AS d INNER JOIN d2l r on r.dateId = d.id INNER JOIN locations l on l.id = r.locID where d.id = ' + i;
	db.all(sql, [], (err, rows) => {
		if(err){
			throw err;
		}
		rows.some(function(row) {
			console.log(row.name);
			return true;
		});
	});
}


db.close();

function getLocation(){
	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(showPosition);
	} else {
		console.log("Geolocation is not supported by this browser");
	}
}

function showPosition(position) {
	console.log(position.coords.latitude);
	console.log(position.coords.longitude);
}

function getRandomDate(){

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

