#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c = 'X') {
    const w = this.width;
    let h = this.height;
    while (h > 0) {
      let temp = '';
      for (let j = 0; j < w; j++) {
        temp += c;
      }
      console.log(temp);
      h--;
    }
  }
}

module.exports = Square;
