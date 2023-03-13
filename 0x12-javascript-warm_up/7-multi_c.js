#!/usr/bin/node
const args = process.argv.slice(2);
const arg0 = args[0];
const str = 'C is fun';
let i;
for (i = 0; i < arg0; i++) {
  console.log(str);
}
