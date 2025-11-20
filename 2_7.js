'use strict';

const query = document.querySelector('#query')
let ul = ''
let dice = 0
const max = parseInt(prompt("How many sides in the dice?"))


function roll_max(max) {

 do {
  dice = Math.floor(Math.random()*max+1)
   ul += `<li>${dice}</li>`
 } while (dice !== max);
}

roll_max(max)
  query.innerHTML = ul