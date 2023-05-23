#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
fs.writeFile(filePath, process.argv[3], 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
