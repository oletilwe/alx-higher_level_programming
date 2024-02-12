#!/usr/bin/node
const add = (a, b) => a + b;

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && !isNaN(arg2)) {
  console.log(`The sum of ${arg1} and ${arg2} is: ${add(arg1, arg2)}`);
} else {
  console.log('Please provide two valid integers.');
}
