#!/usr/bin/node

const arg2 = process.argv[2];

const parsedNum = parseInt(arg2);

console.log(isNaN(parsedNum) ? 'Not a number' : 'My number: ' + parsedNum);
