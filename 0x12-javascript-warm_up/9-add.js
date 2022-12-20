#!/usr/bin/node
function add (a, b) {
  if (a && b) {
    return a + b;
  }
  return NaN;
}
const process = require('process');
const argv = process.argv;
const first = parseInt(argv[2], 10);
const second = parseInt(argv[3], 10);
console.log(add(first, second));
