#!/usr/bin/node
// Import the array from the file
const data = require('./100-data').list;
console.log(data);
const newData = data.map((value, index) => value * index);
console.log(newData);
