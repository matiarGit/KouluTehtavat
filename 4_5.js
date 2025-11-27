'use strict';

async function show_joke() {
  const searchtext = 'https://api.chucknorris.io/jokes/random;'

  try {
      const response = await fetch(searchtext)
    const jsontext = await response.json()
    const joke = jsontext.value
    console.log(joke);

  } catch (error) {
    console.log(error.message)
  }
}

show_joke()