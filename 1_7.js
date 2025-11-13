'use strict';

const dice_rolls = parseInt(prompt("How many dice to roll?"))
let dice_sum = 0

for (let i=1; i <=dice_rolls;i++) {
  const dice = Math.floor(Math.random()*6+1)
  dice_sum += dice
}

document.querySelector('#dice').innerHTML = 'The sum of the dice is ' + dice_sum + '.'