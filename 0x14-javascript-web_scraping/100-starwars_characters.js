#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const id = argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const film = JSON.parse(body);
  for (const charurl of film.characters) {
    request(charurl, (error2, response2, body2) => {
      if (error2) {
        console.error(error2);
      }
      const character = JSON.parse(body2);
      console.log(character.name);
    });
  }
});
