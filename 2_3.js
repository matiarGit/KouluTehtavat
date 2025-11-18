'use strict';

const query = document.querySelector('#query')

const dogs_names = [];

for (let i = 0; i < 6; i++) {
let name = prompt("Name a dog:")
  dogs_names.push(name)

}

dogs_names.sort()

dogs_names.reverse()

let list_text = ''

for (let i = 0; i<6; i++) {

  list_text += `<li>${dogs_names[i]}</li>`

}

query.innerHTML = list_text