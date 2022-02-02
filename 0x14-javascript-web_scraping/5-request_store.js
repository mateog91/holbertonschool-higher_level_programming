#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const fs = require('fs');

const url = argv[2];
const filename = argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
      // file written succesfully
    });
  }
});
