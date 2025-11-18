'use strict';

const numberList = [];

for (let i=0; i<5; i++) {
  let number = parseInt(prompt("Give me a number"))
  numberList[i] = number;
}

for (let i=4; i>=0; i--) {
  console.log(numberList[i])
}