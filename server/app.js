"use strict";

require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const connection = require('./database')

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', (request, response) => {
  
});

module.exports = app;