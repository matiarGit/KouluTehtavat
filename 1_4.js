'use strict';

const house_nmb = Math.floor(Math.random()*4+1)

const name = prompt("What is your name?")

let house

if (house_nmb >= 3) {
  if (house_nmb === 4) {
    house = "Ravenclaw"
  }
  else {
    house = "Hufflepuff"
  }
}
else {
  if (house_nmb === 2) {
    house = "Slytherin"
  }
  else {
    house = "Gryffindor"
  }
}

document.querySelector('#house').innerHTML = name + ', you are ' + house + ".";