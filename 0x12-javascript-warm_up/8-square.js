#!/usr/bin/node
const args = process.argv.slice(2);
const arg0 = args[0];
if (isNaN(arg0)) {
  console.log('Missing size');
} else {
  let i, j;
  for (i = 0; i < arg0; i++) {
    let row = '';
    for (j = 0; j < arg0; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
