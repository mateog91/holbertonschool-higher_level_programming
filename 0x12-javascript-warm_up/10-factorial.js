#!/usr/bin/node

function factorial (a) {
  if (a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}

const { argv } = require('process');
const a = parseInt(argv[2]);
if (a) {
  console.log(factorial(a));
} else {
  console.log(1);
}
