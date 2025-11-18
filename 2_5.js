'use strict';

const numbers_list = []

let number

let x = 0

do {

  number = parseInt(prompt("Give a number: (program will end if you enter a duplicate)"))
  if (numbers_list.includes(number)) {
    x = 1
  }

  else {
    numbers_list.push(number)
  }

} while (x !== 1);

numbers_list.sort()


for (let i=0; i < numbers_list.length; i++) {
  console.log(numbers_list[i])
}
