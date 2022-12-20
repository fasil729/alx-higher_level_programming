#!/usr/bin/node
function factorial (a) {
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
const process = require('process');
const argv = process.argv;
const num = parseInt(argv[2], 10);
if (num) {
  console.log(factorial(num));
} else {
  console.log(factorial(0));
}
