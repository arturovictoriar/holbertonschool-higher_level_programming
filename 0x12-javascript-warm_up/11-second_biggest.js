#!/usr/bin/node
/*
  searche and print the second biggest integer in the list of arguments.
*/
const args = process.argv;
const len = process.argv.length;
if (len > 3) {
  args.sort();
  const secondBiggest = args[len - 2];
  console.log(secondBiggest);
} else {
  console.log(0);
}
