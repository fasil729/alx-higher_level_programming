#!/usr/bin/node
const list = require('./100-data.js').list;
const newlist = list.map(function (element, index) {
  return element * index;
});
console.log(list);
console.log(newlist);
