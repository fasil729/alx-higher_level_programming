#!/usr/bin/node

exports.esrever = function (list) {
  let newl = [];
  for (const el of list[::-1}) {
    newl += el;
  }
  return newl;
}
