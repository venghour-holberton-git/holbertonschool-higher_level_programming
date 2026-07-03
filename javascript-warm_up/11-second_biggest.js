#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < args.length; i++) {
    const n = args[i];

    if (n > max) {
      secondMax = max;
      max = n;
    } else if (n > secondMax && n < max) {
      secondMax = n;
    }
  }

  console.log(secondMax === -Infinity ? 0 : secondMax);
}
