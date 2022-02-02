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
    fs.watchFile(filename, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
