'use strict';

const form = document.querySelector("#form_id");
const query = document.querySelector('#query');
const results = document.querySelector('#results');

async function show_displayer(z) {
  z.preventDefault();
  const searchtext = 'https://api.tvmaze.com/search/shows?q=' + query.value;

  try {
      const response = await fetch(searchtext)
    const jsontext = await response.json()
    console.log(jsontext);

      results.innerHTML = '';
      for (const tvShow of jsontext) {
        const h2 = document.createElement('h2');
        h2.innerText = tvShow.show.name;
        const img = document.createElement('img');
        img.src = tvShow.show.image?.medium;
        img.alt = tvShow.show.name;
        const a = document.createElement('a');
        a.href = tvShow.show.url;
        a.innerText = 'Go to TV Show';
        const div = document.createElement('div');
        div.innerHTML = tvShow.show.summary;
        const article = document.createElement('article');
        article.append(h2,img,div,a);
        results.append(article);


      }
  } catch (error) {
    console.log(error.message)
  }
}

form.addEventListener('submit', show_displayer);