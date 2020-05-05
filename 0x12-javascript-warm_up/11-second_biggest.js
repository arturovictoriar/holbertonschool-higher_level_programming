#!/usr/bin/node
/*
  searche and print the second biggest integer in the list of arguments.
*/
const args = process.argv;
if (args.length > 3) {
  args.sort();
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
