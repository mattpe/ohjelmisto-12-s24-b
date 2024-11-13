'use strict';
console.log('moro');

// taultukot  eli arrays
const items = [1, 2, 3, {name: 'Ulla'}, [3, 4, 5], 'merkkijono'];
console.log(items);

// alkioo viitataan ihan perus indeksillä
console.log(items[0]);
// alkion arvoa voidaan muuttaa tai lisätä indeksin avulla
items[0] = 99;
console.log(items);
items[9] = 'Olen uusi jäsen';

// välissä on nyt ns määrittelemätön arvo/alkio eli undefined
console.log(items[6]);

console.log('Taulukon pituus:', items.length);

// Taulukoiden läpikäynti loopin avulla, yleinen tapa kun halutaan indeksi
console.log('--------------------------');
console.log('Perinteinen for looppi');

for (let i = 0; i < items.length; i++) {
  console.log(i, items[i]);
}

// Ei käytetä juurikaan taulukoiden kanssa, mutta JS objektien/olioiden
console.log('--------------------------');
console.log('Läpikäynti for/in rakenteella, jolla saadaan avain/indeksi ja arvo');
for (const index in items) {
  console.log(index, items[index]);
}

// Helppo ja nopea tapa iteroida läpi taulukko mikäli indeksiä ei tarvita
console.log('--------------------------');
console.log('Läpikäynti for/of rakenteella, jolla saadaan arvot');
for (const item of items) {
  // if lause jossa tutkitaa onko alkio undefined
  if (item != undefined) {
    console.log(item);
  }
}

const names = ['Frank', 'Scott', 'Jasmine', 'Don'];
const ages = [230000,28,32,101];

for (let name of names) {
  console.log(`Name: ${name}`);
}

/*
sort() sorts the array alphabetically
reverse() reverses the items in the array in reverse order
shift() deletes and returns the 1st item in the array
pop() deletes and returns the last item in the array
push(value) adds the value at the end of the array, multiple values separated by commas
includes(value) checks whether the array contains the given value
 */

// järjestä aakkosjärjestykseen
names.sort();
console.log(names);
names.reverse()
console.log(names);

// ei toimi numeroiden kanssa sellaisenaan
ages.sort()
console.log(ages);

// tämä toimii numeroiden kanssa
ages.sort((a, b) => a - b);
console.log(ages);
ages.sort((a, b) => b - a);
console.log(ages);

// lisätään nimi taulukon loppuun
names.push('Iines');
// palauttaa taulukon pituuden
const newLength = names.push('Ulla');
console.log(names);
console.log('Taulukon pituus', newLength);

// lisätään taulukon alkuun
names.unshift('Matti');
console.log(names);

// poistetaan taulukon vika ja otetaan muttujaan talteen
const lastName = names.pop();
console.log('Poistettiin:',lastName)
console.log(names);

// poistetaan taulukon eka ja otetaan muttujaan talteen
const firstName = names.shift();
console.log('Poistettiin:',firstName)
console.log(names);

// etsitään onko taulukossa ko. arvo palauttaa true/false
console.log(names.includes('Scott'));

// object literal eli olio
// samankaltainen kun pythonin sanakirja

const duck = {
  name: 'Aku',
  age: 313,
}
console.log(duck);
console.log(duck['age']);

// muutetaan arvoja
duck['age'] = 36;
duck.name = 'Aku Ankka';

// tietyn ominaisuuden arvon hakeminen
let moikkaus = `Moikkamoi ja tänne muuttuja ${duck.name}`;
let moikkaus2 = duck.name + ' on ' + duck.age + ' ikäinen ja motto: ' + duck.profession;

// lisätään uusi ominaisuuksia
duck.profession = 'working like a duck';
console.log(duck);

// metodin luominen olioon ns. nimettömänä funktiona

const duck2 = {
  name: 'Iiines',
  age: 34,
  getInfo: function() {
    return this.name + ' on ' + this.age + '-vuotias';
  }
}
console.log(duck2.getInfo());

// JS funktiot

// perinteinen funktiomäärittely
function greet(name) {
  console.log(`Greetings ${name}!!!!!`);
  return;
}

// function expression. Funtio joka on anonyymi mutta tallennetaan muuttujaan
const greet2 = function(name) {
  console.log(`Greetings again ${name}!!!`);
}

// arrow funktio / nuolifunktio, edellistä yksikertaisempi ja lyhyempi
const greet3 = (name) => {
  console.log(`Greetings a third time ${name}!!!`);
}

greet('Ulla');
greet2('Ulla');
greet3('Ulla');

const nimi = 'Matti';
function logName() {
  const nimi2 = 'Ulla'
  console.log(nimi);
  console.log(nimi2);
}
console.log(nimi2);
logName();














