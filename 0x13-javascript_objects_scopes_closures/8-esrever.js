#!/usr/bin/node

exports.esrever = function (list) {
  const newl = [];
  for (let el = list.length - 1; el >= 0; el--) {
    newl.push(list[el]);
  }
  return newl;
};
