#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const cha = data.characters;
  for (const i of cha) {
    request.get(i, function (err, res, body1) {
      if (err) {
        console.log(err);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
