'use strict';

const query = document.querySelector('#query')
let ul = ''
let dice = 0

function roll_6() {

 do {
  dice = Math.floor(Math.random()*6+1)
   ul += `<li>${dice}</li>`
 } while (dice !== 6);
}

roll_6()
  query.innerHTML = ul