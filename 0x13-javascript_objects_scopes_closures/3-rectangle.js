#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let e = '';
      for (let j = 0; j < this.width; j++) {
        e += 'X';
      }
      console.log(e);
    }
  }
}

module.exports = Rectangle;
