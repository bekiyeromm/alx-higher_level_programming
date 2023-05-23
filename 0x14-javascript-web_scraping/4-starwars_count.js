#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, (error, resp, body) => {
  body = JSON.parse(body).results;
  if (error) {
    console.log(error);
  } else {
    let countt = 0;
    for (const film of body) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          countt++;
        }
      }
    }
    console.log(countt);
  }
});
