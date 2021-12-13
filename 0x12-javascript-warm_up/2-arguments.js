#!/usr/bin/node
import { argv } from 'process';

let argv_length = argv.length;
if (argv > 0) {
    console.log('Argument found');
} else {
    console.log('No argument')
}
