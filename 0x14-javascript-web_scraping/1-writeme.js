#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const filename = argv[2];
const content = argv[3];

fs.writeFile(filename, content, err => {
    if (err) {
        console.error(err)
        return
    }
    //file written successfully
});
