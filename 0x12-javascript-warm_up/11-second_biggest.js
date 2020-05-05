#!/usr/bin/node
/*
  searche and print the second biggest integer in the list of arguments.
*/
const args = process.argv;
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  args.sort();
  console.log(args[len - 2]);
}
