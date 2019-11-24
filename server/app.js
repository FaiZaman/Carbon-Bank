"use strict";

require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const morgan = require('morgan');
const connection = require('./database')

const app = express();
app.use(morgan('combined'));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

app.get('/', (request, response)=> {
  response.send("Hello World!");
});

app.get('/query', (request, response) => {
  connection.query("SELECT * FROM users;",
    function(error, results){
      if (error) throw error;
      response.json(results);
    }
  );
});

module.exports = app;