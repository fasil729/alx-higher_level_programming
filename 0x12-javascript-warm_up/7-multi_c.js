#!/usr/bin/node
const process = require('process');
const argv = process.argv;
let num = parseInt(argv[2], 10);
if (!argv[2]) {
  console.log('Missing number of occurrences');
}
while (num > 0) {
  console.log('C is fun');
  num--;
}
