#!/usr/bin/node

const args = process.argv.slice(2);
let second_big = 0;

if (args.length > 1) {
  const ints = args.map(Number);
  integers.sort((a, b) => b - a);
  second_big = ints[1];
}

console.log(second_big);
