#!/usr/bin/node


const fs = require('fs');
const file = process.argv[2]
const str = process.argv[3];

fs.writeFile(file, str, 'utf-8', function(err) {
    if (err) {
        console.error(err);
    } else {
        console.log(str);
    }
});
