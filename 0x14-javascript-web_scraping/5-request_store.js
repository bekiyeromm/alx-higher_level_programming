#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const pathUrl = process.argv[2];
const filePath = process.argv[3];
request.get(pathUrl, function (error, resp, body) {
  if (error) throw error;
  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) throw err;
  });
});
