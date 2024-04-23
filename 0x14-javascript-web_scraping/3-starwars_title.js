#!/usr/bin/node

const request = require('request');
const mv_name = process.argv[2];
const api_link = 'https://swapi-api.hbtn.io/api/films/';

request(api_link + mv_name, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
