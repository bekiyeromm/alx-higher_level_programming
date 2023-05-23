#!/usr/bin/node
// const fs = require('fs');
const request = require('request');
const pathUrl = process.argv[2];

request.get(pathUrl, function (error, resp, body) {
  if (error) throw error;
  const user = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (user[task.userId]) {
        user[task.userId]++;
      } else {
        user[task.userId] = 1;
      }
    }
  }
  console.log(user);
});
