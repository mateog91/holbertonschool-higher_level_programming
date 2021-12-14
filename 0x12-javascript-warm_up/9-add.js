#!/usr/bin/node
const { argv } = require('process');

function add(a, b) {
  return (a + b);
}

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
if (b) {
  console.log(add(a, b));
} else {
  console.log(b);
}
