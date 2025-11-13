'use strict';

const number1 = parseInt(prompt("Anna ensimmäinen numero"))
const number2 = parseInt(prompt("Anna toinen numero"))
const number3 = parseInt(prompt("Anna kolmas numero"))

const summa = number1 + number2 + number3
const tulo = number1 * number2 * number3
const keskiarvo = summa / 3

document.querySelector('#summa').innerHTML = 'Summa = ' + summa.toString();
document.querySelector('#tulo').innerHTML = 'Tulo = ' + tulo.toString();
document.querySelector('#keskiarvo').innerHTML = 'Keskiarvo =' + keskiarvo.toString();