#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;
    for (const film of films) {
      const characters = film.characters;
      for (const char of characters) {
        if (char.includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
