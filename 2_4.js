'use strict';

const number_list = []

let number

do {

  number = parseInt(prompt("Give a number: (0 if you want to stop)"))
  number_list.push(number)

} while (number !== 0);

number_list.sort()
number_list.reverse()

for (let i=0; i < number_list.length-1; i++) {
  console.log(number_list[i])
}
