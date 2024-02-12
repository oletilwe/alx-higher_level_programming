#!/usr/bin/node
const computeFactorial = (n) => {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }
  if (n === 0 || n === 1) {
    return 1; // Base case: factorial of 0 or 1 is 1
  } else {
    return n * computeFactorial(n - 1); // Recursive case
  }
};

const argument = parseInt(process.argv[2]);
console.log(`Factorial of ${argument} is: ${computeFactorial(argument)}`);
