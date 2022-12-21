#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const w = this.width;
    let h = this.height;
    while (h > 0) {
      let temp = '';
      for (let j = 0; j < w; j++) {
        temp += 'X';
      }
      console.log(temp);
      h--;
    }
  }
}

module.exports = Rectangle;
