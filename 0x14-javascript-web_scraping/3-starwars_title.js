#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const fullUri = 'https://swapi-api.hbtn.io/api/films/'.concat(movieId);

request.get(fullUri, (error, resp, body) => {
  body = JSON.parse(body);
  if (error) {
    console.log(error);
  } else {
    console.log(body.title);
  }
});
