#!/usr/bin/node
const fs = require('fs');

// Get the file paths from the command line arguments
const [, , sourceFile1, sourceFile2, destination] = process.argv;

// Read the contents of the source files
const data1 = fs.readFileSync(sourceFile1);
const data2 = fs.readFileSync(sourceFile2);

// Concatenate the contents of the source files
const concatenatedData = Buffer.concat([data1, data2]);

// Write the concatenated data to the destination file
fs.writeFileSync(destination, concatenatedData);
