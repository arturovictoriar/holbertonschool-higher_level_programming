#!/usr/bin/node
/*
    Class Square
    inherit from Rectangle
    create a charPrint(c) method
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let height = 0; height < this.height; height++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
