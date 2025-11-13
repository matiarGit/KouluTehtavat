'use strict';

const question = confirm("Should I calculate the square root?")

if (question === true) {
  const number = parseInt(prompt("Number:"))
  if (number < 0) {
    document.querySelector('#sqrt').innerHTML = 'The square root of a negative number is not defined.'
  }
  else {
    const sqrt_nmb = Math.sqrt(number)
    document.querySelector('#sqrt').innerHTML = 'The square root of ' + number + ' is ' + sqrt_nmb + '.'
  }
}

else if (question === false) {
  document.querySelector('#sqrt').innerHTML = 'The square root is not calculated.'
}