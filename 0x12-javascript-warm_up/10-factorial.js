#!/usr/bin/node
const args = process.argv.slice(2);
const num = Number(args[0]);
function factorial (num) {
  if (isNaN(num) || (num === 0)) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(num));
