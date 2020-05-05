#!/usr/bin/node
/*
  print first input argument
*/
const args = process.argv;
if (args.length <= 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
