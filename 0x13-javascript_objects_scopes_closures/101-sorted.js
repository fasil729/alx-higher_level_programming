#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};
for (const item in dict) {
  if (!newDict[dict[item]]) {
    newDict[dict[item]] = [];
  }
  newDict[dict[item]].push(item);
}
console.log(newDict);
