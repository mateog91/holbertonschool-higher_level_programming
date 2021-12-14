#!/usr/bin/node
/** Define Rectangle class */
const Square1 = require('./5-square.js');

module.exports = class Square extends Square1 {
  charPrint (c) {
    let str = 'X';
    if (c) {
      str = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(str.repeat(this.width));
    }
  }
};
