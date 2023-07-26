#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) throw error;

  const completedTasksByUser = {};

  body.forEach(task => {
    if (task.completed) {
      if (completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId]++;
      } else {
        completedTasksByUser[task.userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});
