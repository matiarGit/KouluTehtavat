'use strict';

const trigger = document.querySelector('#trigger')
const target = document.querySelector('#target')

function mouseover_function() {
  target.src = "picB.jpg"
}
function mouseleave_function() {
  target.src = "picA.jpg"
}

trigger.addEventListener('mouseover',mouseover_function)
trigger.addEventListener('mouseleave',mouseleave_function)





