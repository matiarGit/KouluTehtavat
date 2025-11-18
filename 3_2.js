'use strict';

const query = document.querySelector('#target');

const text1 = document.createTextNode('First item');
const text2 = document.createTextNode('Second item');
const text3 = document.createTextNode('Third item');

const li1 = document.createElement('li')
const li2 = document.createElement('li')
const li3 = document.createElement('li')

li1.appendChild(text1)
li2.appendChild(text2)
li3.appendChild(text3)

li2.classList.add('my-item')

query.appendChild(li1)
query.appendChild(li2)
query.appendChild(li3)