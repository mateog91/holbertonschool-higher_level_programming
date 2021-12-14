#!/usr/bin/node
const { argv } = require('process');

const argv1 = parseInt(argv[2]);

if (isNaN(argv1)) {
  console.log('Missing size');
} else if (argv1 > 0) {
  for (let i = 0; i < argv1; i++) {
    const arr = [];
    for (let j = 0; j < argv1; j++) {
      arr.push('X');
    }
    console.log(arr.join(''));
  }
}
