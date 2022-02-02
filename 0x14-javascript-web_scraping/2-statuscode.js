#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = argv[2];

request(url, (error, res) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
