#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (parseInt(argv[2], 10)) {
  console.log('My number:', parseInt(argv[2], 10));
} else {
  console.log('Not a number');
}
