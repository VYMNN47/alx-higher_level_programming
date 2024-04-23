#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request(link, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const filmChars = films[film].characters;
      for (const character in filmChars) {
        if (filmChars[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
