#!/usr/bin/node
const { argv } = require('process');

if (argv[3]) {
  const sorted = argv.sort((a, b) => a - b);
  console.log(sorted[sorted.length - 2]);
} else {
  console.log(0);
}
