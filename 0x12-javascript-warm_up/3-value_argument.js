#!/usr/bin/node
const { argv } = require('process');

let flag = 0;
argv.forEach((val, index) => {
  if (index === 2) {
    console.log(argv[2]);
    flag = 1;
  }
});
if (flag === 0) {
  console.log('No argument');
}
