#!/usr/bin/node

const args = process.argv;
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  args.sort();
  const secondBig = args[len - 2];
  console.log(secondBig);
}
