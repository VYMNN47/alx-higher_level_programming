#!/usr/bin/node

const argsLen = process.argv.length;

if (argsLen === 2) {
    console.log("No arguments");
} else if (argsLen === 3) {
    console.log("Exactly one argument found");
} else {
    console.log("More than one argument found");
}

