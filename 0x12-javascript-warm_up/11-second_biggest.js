#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (!argv[3]) {
  console.log(0);
} else {
  for (let num = 2; num < argv.length; num++) {
    let count = 0;
    for (let i = 2; i < argv.length; i++) {
      if (parseInt(argv[num]) < parseInt(argv[i])) {
        count += 1;
      }
    }
    if (count === 1) {
      console.log(argv[num]);
      break;
    }
  }
}
