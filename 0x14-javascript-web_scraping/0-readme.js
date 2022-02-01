#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const filename = argv[2];

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
