#!/usr/bin/node
/*
  searche and print the second biggest integer in the list of arguments.
*/
const args = process.argv;
if (args.length > 3) {
  const orderArrayNum = args.filter((num, index) => index > 1).sort();
  console.log(orderArrayNum[orderArrayNum.length - 2]);
} else {
  console.log(0);
}
