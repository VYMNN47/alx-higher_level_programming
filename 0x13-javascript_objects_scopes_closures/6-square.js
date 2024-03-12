#!/usr/bin/node
const SquareC = require('./5-square');

class Square extends SquareC {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let e = '';
      for (let j = 0; j < this.width; j++) {
        e += c;
      }
      console.log(e);
    }
  }
}

module.exports = Square;
