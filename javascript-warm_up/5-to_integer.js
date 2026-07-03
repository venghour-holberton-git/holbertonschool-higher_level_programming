#!/usr/bin/node

const value = process.argv[2];

if (value === undefined) {
  console.log('Not a number');
} else {
  const num = Number(value);

  if (Number.isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + num);
  }
}
