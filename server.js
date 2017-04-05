// Created by Nicholas Gregorio and Janahan Mathanamohan
// server.js

// Intial requirements for the server
var  express = require('express');
var app = express();
var port = process.env.PORT || 8080;
var bodyParser = require("body-parser");
var flash = require('connect-flash');
var cookieParser = require('cookie-parser');

// Setting up the server and the simple front end
app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({"extended" : false}));
app.use(flash());

// Starting the server
require('./app/routes.js')(app);
app.listen(8081);
