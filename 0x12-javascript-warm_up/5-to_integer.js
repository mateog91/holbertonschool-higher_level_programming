#!/usr/bin/node
const { argv } = require('process');

const argv1 = parseInt(argv[2]);
if (isNaN(argv1)) {
  console.log('Not a number');
} else {
  console.log((argv1));
}
