#!/usr/bin/node
const { argv } = require('process');

const argv1 = parseInt(argv[2]);
if (isNaN(argv1)) {
  console.log('Missing number of occurrences');
} else if (argv1 > 0) {
  for (let i = 0; i < argv1; i++) {
    console.log('C is fun');
  }
}
