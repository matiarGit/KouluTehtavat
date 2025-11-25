'use strict'

const form = document.querySelector('#source');
const firstname = document.querySelector('input[name=firstname]');
const lastname = document.querySelector('input[name=lastname]');
const p = document.querySelector('p');

function text_maker(z) {
  z.preventDefault();
   p.innerText = `Your name is ${firstname.value} ${lastname.value}`;
}

form.addEventListener('submit', text_maker)