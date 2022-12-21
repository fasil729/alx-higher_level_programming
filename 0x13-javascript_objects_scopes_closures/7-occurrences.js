#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (const el of list) {
    if (el === searchElement) {
      c += 1;
    }
  }
  return c;
};
