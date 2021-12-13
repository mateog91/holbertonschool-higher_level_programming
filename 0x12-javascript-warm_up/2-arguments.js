#!/usr/bin/node
const { argv } = require('process');

if (argv.length > 3) {
  console.log('Arguments found');
} else if (argv.length > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
