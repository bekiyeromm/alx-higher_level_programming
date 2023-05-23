#!/usr/bin/node
const req = require('request');
const urlPath = process.argv[2];
req.get(urlPath, (error, resp) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', resp.statusCode);
  }
});
