'use strict';

const query = document.querySelector('#target');
const html = `<li>First Item</li>
<li>Second Item</li>
<li>Third Item</li>`;

query.innerHTML = html;
query.classList.add('my-list')