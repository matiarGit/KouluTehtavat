'use strict';

const year = parseInt(prompt("Year:"))

let is_it

if (year % 4 === 0) {
  if (year % 100 === 0) {
    if (year % 400 === 0) {
      is_it = "It's a leap year."
    }
     else {
       is_it = "It's not a leap year."
    }
  }
  else{
    is_it = "It's a leap year."
  }
}
else {
  is_it = "It's not a leap year."
}

document.querySelector('#leapyear').innerHTML = is_it;