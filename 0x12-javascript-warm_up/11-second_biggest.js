#!/usr/bin/node
const findSecondBiggest = (args) => {
  const integers = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));

  if (integers.length < 2) {
    return 0;
  }

  integers.sort((a, b) => b - a);
  return integers[1];
};

const argumentsList = process.argv.slice(2);
const secondBiggest = findSecondBiggest(argumentsList);

console.log(`Second biggest integer: ${secondBiggest}`);
