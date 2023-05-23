#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const fullUri = 'https://swapi-api.hbtn.io/api/films/'.concat(movieId);

request.get(fullUri, (error, resp, body) => {
  body = JSON.parse(body);
  if (error) throw error;
  for (const film of body.characters) {
    request(film, function (error, resp, body) {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  }
});
