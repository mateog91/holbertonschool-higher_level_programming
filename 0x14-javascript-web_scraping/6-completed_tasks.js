#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const obj = JSON.parse(body);
    const d = {};
    for (const task of obj) {
      if (task.completed) {
        if (d[task.userId]) {
          d[task.userId] += 1;
        } else {
          d[task.userId] = 1;
        }
      }
    }
    console.log(d);
  }
});
