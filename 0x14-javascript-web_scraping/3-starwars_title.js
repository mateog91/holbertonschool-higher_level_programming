#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const id = argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(`${data.title}`);
  }
});
