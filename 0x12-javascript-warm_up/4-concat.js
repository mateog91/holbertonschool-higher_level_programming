#!/usr/bin/node
const { argv } = require('process');

let argv1 = 'undefined';
let argv2 = 'undefined';
argv.forEach((val, index) => {
    if (index === 2) {
        argv1 = val;
    }
    if (index === 3) {
        argv2 = val;
    }
});
console.log(`${argv1} is ${argv2}`);
