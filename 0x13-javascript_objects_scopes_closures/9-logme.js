#!/usr/bin/node
/*
     prints the number of arguments already printed and the new argument value
*/
let count = 0;
exports.logMe = function (item) {
  count += 1;
  console.log(`${count}: ${item}`);
};
