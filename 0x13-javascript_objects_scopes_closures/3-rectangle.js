#!/usr/bin/node
/** Define Rectangle class */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const str = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(str.repeat(this.width));
    }
  }
};
