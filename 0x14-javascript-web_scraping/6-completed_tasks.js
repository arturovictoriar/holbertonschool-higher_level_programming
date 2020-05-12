#!/usr/bin/node
/*
    computes the number of tasks completed by user id
*/
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    const dictCompletTodoUser = {};
    for (const todo of jsonBody) {
      if (dictCompletTodoUser[todo.userId]) {
        if (todo.completed) {
          dictCompletTodoUser[todo.userId] += 1;
        }
      } else {
        if (todo.completed) {
          dictCompletTodoUser[todo.userId] = 1;
        } else {
          dictCompletTodoUser[todo.userId] = 0;
        }
      }
    }
    console.log(dictCompletTodoUser);
  }
});
