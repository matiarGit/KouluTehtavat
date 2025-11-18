'use strict';

function calculate() {
 let what_to_calculate = document.getElementById('operation').value;

 const number1 = parseInt(document.querySelector('#num1').value);
 const number2 = parseInt(document.querySelector('#num2').value);

 let result = 0


switch (what_to_calculate) {
  case 'add':
    result = number1 + number2;
    break;

  case 'sub':
    result = number1 - number2;
    break;

  case 'multi':
    result = number1 * number2;
    break;

  case 'div':
    result = number1 / number2;
    break;

  default:
    console.log('Something went wrong.');
}

 document.getElementById('result').innerHTML = result;

}