#!/usr/bin/node

const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count > 3 ? 'Arguments found' : 'Argument found');
