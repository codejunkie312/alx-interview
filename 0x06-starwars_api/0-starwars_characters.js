#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
let people = [];
const characters = [];

async function getPeople () {
  await new Promise(resolve => request(url, (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      const jsonBody = JSON.parse(body);
      people = jsonBody.characters;
      resolve();
    }
  }));
}

async function getCharacters () {
  for (const person of people) {
    await new Promise(resolve => request(person, (err, res, body) => {
      if (err) {
        console.error(err);
      } else {
        const jsonBody = JSON.parse(body);
        characters.push(jsonBody.name);
        resolve();
      }
    }));
  }
}

async function main () {
  await getPeople();
  await getCharacters();

  characters.forEach(character => {
    console.log(character);
  });
}

main();
