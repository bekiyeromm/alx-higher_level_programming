#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const fullUri = 'https://swapi-api.hbtn.io/api/films/'.concat(movieId);

request.get(fullUri, (error, resp, body) => {
  body = JSON.parse(body);
  if (error) throw error;
  else {
    callFun(body.characters, 0);
  }
}
);
function callFun (person, index) {
  if (index >= person.length) {
    return;
  }
  request(person[index], (error, response, bd) => {
    if (error) throw error;
    else {
      console.log(JSON.parse(bd).name);
      return callFun(person, ++index);
    }
  });
}
