const mysql = require('mysql');

// local connection

let connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USERNAME,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD
});

connection.connect(function(error){
  if (error){
    console.log("Error connecting: " + error.stack);
    return;
  }
  console.log("Connected as thread ID " + connection.threadId);
});

module.exports = connection;