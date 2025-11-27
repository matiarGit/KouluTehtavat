'use strict';

const form = document.querySelector("#form_id");
const query = document.querySelector('#query');

async function text_maker(z) {
  z.preventDefault();
  const searchtext = 'https://api.tvmaze.com/search/shows?q=' + query.value;
  const response = await fetch(searchtext)
  const jsontext = await response.json()
console.log(jsontext);
}

form.addEventListener('submit', text_maker);