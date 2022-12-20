#!/usr/bin/node
const process = require('process');
const argv = process.argv;
let num = parseInt(argv[2], 10);
if (!num) {
  console.log('Missing size');
}
const i = num;
while (num > 0) {
  let temp = '';
  for (let j = 0; j < i; j++) {
    temp += 'X';
  }
  console.log(temp);
  num--;
}
