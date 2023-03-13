#!/usr/bin/node
const args = process.argv.slice(2);

// Check if there are no arguments
if (args.length === 0) {
  console.log(0);
}
// Check if there is only one argument
else if (args.length === 1) {
  console.log(0);
} else {
  // Convert arguments to integers
  const integers = args.map(arg => parseInt(arg, 10));

  // Find the second biggest integer
  const sortedIntegers = integers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
}
