#!/usr/bin/node
const { argv } = require('process');

const argv1 = argv[2];
if (isNaN(argv1)) {
  console.log('Not a number');
} else {
  console.log(parseInt(argv1));
}
