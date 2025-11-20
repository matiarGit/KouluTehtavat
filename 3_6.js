'use strict';

const button = document.querySelector('button')


function tapahtumakasittelija(){
   alert('Button clicked');
}

button.addEventListener('click',tapahtumakasittelija)