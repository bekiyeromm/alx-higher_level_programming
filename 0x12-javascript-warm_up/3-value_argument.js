#!/usr/bin/node
const args = process.argv.slice(2);
const arg0 = args[0];
if (arg0) {
  console.log(arg0);
} else {
  console.log('No argument');
}
