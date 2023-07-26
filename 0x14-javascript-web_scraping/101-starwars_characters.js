#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) throw error;

  const characterUrls = body.characters;
  const characters = [];

  let completedRequests = 0;

  characterUrls.forEach(url => {
    request(url, { json: true }, (error, response, body) => {
      if (error) throw error;

      characters[body.url.match(/\d+/)[0] - 1] = body.name;

      completedRequests++;

      if (completedRequests === characterUrls.length) {
        console.log(characters.join('\n'));
      }
    });
  });
});
