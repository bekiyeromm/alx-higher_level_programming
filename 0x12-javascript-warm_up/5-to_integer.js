#!/usr/bin/node
const args = process.argv.slice(2);
const arg0 = args[0];
if (!isNaN(parseInt(arg0))) {
  console.log(`My number: ${parseInt(arg0)}`);
} else {
  console.log('Not a number');
}
