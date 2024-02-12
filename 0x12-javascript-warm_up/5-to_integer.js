#!/usr/bin/node
const args = process.argv.slice(2);

const parsedNumber = parseInt(args[0]);

if (!isNaN(parsedNumber)) {
  console.log(`My number: ${parsedNumber}`);
} else {
  console.log('Not a number');
}
