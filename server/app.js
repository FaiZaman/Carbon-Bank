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
  let user;
  let i;
  for (user = 1; user < 4; user++){
    for (i = 0; i < 30; i++){
      let date = Math.floor(Math.random() * (23) + 1);
      const transdate = "2019-11-" + date;
      const flow = Math.round(Math.random());
      const cat = Math.floor(Math.random() * (7) + 1);
      let amount = 0;
      const smallAmount = Math.floor(Math.random() * (5, 20)) + 20;
      const largeAmount = Math.floor(Math.random() * (100, 500));
      const probability = Math.random();
      if (probability > 0.05){
        amount = smallAmount;
      }
      else{
        amount = largeAmount;
      }
      connection.query("INSERT INTO transactions (transdate, flow, cat, usID, amount) values (" + "'" + transdate + "', " + flow + ", " + cat + ", " + user + "," + amount + ");",
        function(error, results){
          if (error) throw error;
        }
      );
    }
  }
});

app.get('/calculate', (request, response) => {

  connection.query("SELECT amount FROM transactions WHERE cat = 2",
    function(error, results){
      if (error) throw error;
      for (let i = 0; i < results.length; i++){
        let price = results[i].amount;
        price = fuelCostCalculator(price);
      }
    }
  )
});

function fuelCostCalculator(amount){
  const litreFuelCost = 1.189
  let totalCost = (amount/litreFuelCost) * 2.3 // value per footprint
  return totalCost.toFixed(2);
}

module.exports = app;