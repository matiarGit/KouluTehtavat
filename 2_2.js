'use strict';

const query = document.querySelector('#query')

const participants_nmb = parseInt(prompt("How many participants?"))

const participants_names = [];

for (let i = 0; i <participants_nmb; i++) {
let name = prompt("Name:")
  participants_names.push(name)

}

participants_names.sort()

let list_text = ''

for (let i = 0; i<participants_nmb; i++) {

  list_text += `<li>${participants_names[i]}</li>`

}

query.innerHTML = list_text