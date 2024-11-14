'use strict';

/* Write a program that asks the user for the number of participants.
After this, the program asks for the names of all participants.
Finally, the program prints the names of the participants on the
web page in an ordered list (<ol>) in alphabetical order. (2p)
 */
console.log('Assignments:');

const nlist = document.querySelector('.namelist');
console.log(nlist);
// nlist.innerHTML = '<li>Ulla</li><li>Anna</li><li>Tapsa</li>';
let inner = '';

const num = parseInt(prompt('Please give me a number of participants: '));
const names = [];

function askNames() {

  for (let i = 0; i < num; i++) {
    console.log(i);
    let name = prompt('Please give me a name');
    names.push(name);
  }
  console.log(names);
}

function printNames() {
  // printata konsoliin, 2 eri tapaaa

  console.log(names.length);

  // versio 1. käytetään for looppia ja innerHTML
  for (let i = 0; i < names.length; i++) {
      console.log(names[i]);
      inner += `<li>${names[i]}</li>`
  }
  console.log(inner);
  nlist.innerHTML = inner;

  // versio 2. käytetään for/of ja create element
  for (let name of names) {
    console.log(name);
    // <li></li>
    let liElement = document.createElement('li');
    // <li>name</li>
    liElement.innerHTML = name;
    nlist.appendChild(liElement);
  }
}

askNames();
printNames();

