// haetaan viittaus johon solmuun (node) DOMissa
const h1Elem = document.querySelector('h1');
console.log(h1Elem);
// Muokataa DOMia
const title = h1Elem.textContent;
h1Elem.textContent = title + ' + lisäys otsikkoon';
h1Elem.style.fontSize = '22px';
h1Elem.classList.add('text');
//piilotetaan elementti css:n avulla
h1Elem.classList.add('hidden');
// näytetään taas
h1Elem.classList.remove('hidden');
// ylemmän tason parent-elementin piilotus
//h1Elem.parentElement.classList.add('hidden');

// lisätään sisältöä sivulle
const pElem = document.createElement('p');
document.querySelector('main').append(pElem);
pElem.textContent = 'Uusi kappale by JS!';

// haetaan viittaus useampaan elementtiin/nodeen kerralla
const paragraphs = document.querySelectorAll('p');
//console.log(paragraphs);
paragraphs[2].textContent = 'Kolmas kappale.';
/* iteroidaan kaikki kappaleet läpi
for (const p of paragraphs) {
    p.textContent = 'päivitetty!';
}
*/

// Tehdään järjestetty lista jossa 5 alkiota
const listContents = ['kynä', 'kumi', 'reppu', 'pulpetti'];

// haetaan viittaus diviin id:n avulla
const listDiv = document.querySelector('#list');

// funktio jolla voi tulostaa taulukon sisällön ol-listaksi DOMiin
// ottaa paramatetrina taulukon, jonka alkioista lista luodaan
function renderList(items) {
  // tyhjennetää div ennen uuden ol-elementin lisäystä
  listDiv.innerHTML = '';
  const olElement = document.createElement('ol');
  for (let i = 0; i < items.length; i++) {
    const newLi = document.createElement('li');
    newLi.textContent = items[i];
    olElement.append(newLi);
  }
  listDiv.append(olElement);
}

//renderList(listContents);
//listContents.push('tietskari');

// BOM-rajapinta (window-olio)
// luetaan selaimen "sijainti" (URL)
window.console.log(window.location.href);
// siirrytään johonkin toiseen osoitteeseen
//window.location.href = 'https://www.google.fi';

// Tapahtumankäsittely eli eventit
const printButton = document.querySelector('#print');
// asetetaan napille tapahtumankäsittelelijä click-eventille
printButton.addEventListener('click', function(event) {
  console.log('print & sort button clicked, event: ', event);
  listContents.sort();
  renderList(listContents);
});
// asioiden lisäys listalle
const addButton = document.querySelector('#add');
// asetetaan napille tapahtumankäsittelelijä click-eventille
addButton.addEventListener('click', () => {
  const newItem = window.prompt('Lisää jotain listaan?');
  listContents.push(newItem);
  renderList(listContents);
});

// Hiiritapahtumia
document.addEventListener('mousemove', function(event) {
  //console.log(event);
  document.querySelector('#output').textContent = `Hiiren
        osoittimen koordinaatit: ${event.clientX}, ${event.clientY}`;
  // näytetään h1, kun hiiri menee riittävän alas dokumentilal
  if (event.clientY > 300) {
    h1Elem.classList.remove('hidden');
  }
});

h1Elem.addEventListener('mouseenter', function() {
  // piilotetaan elementti css avulla, kun hiiren osoitin menee sen päälle
  h1Elem.classList.add('hidden');
});

// Näppiseventti "toggle" (h piilottaa ja näyttää koko sivun)
const keyLog = [];
let hidden = false;
document.addEventListener('keypress', function(event) {
  //console.log('näppäin: ', event.key);
  keyLog.push(event.key);
  console.log('logi', keyLog);
  if (event.key === 'h') {
    if (!hidden) {
      document.querySelector('body').classList.add('hidden');
    } else {
      document.querySelector('body').classList.remove('hidden');
    }
    hidden = !hidden;
  }
});

// Oletustapahtuma ja sen estäminen
// estetään formin automaattinen lähetys (sivun päivitys)
const form = document.querySelector('form');
const fname = document.querySelector('input[name=fName]');
const lname = document.querySelector('input[name=lName]');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  console.log(event);
  console.log('Etunimi:', fname.value);
  console.log('Sukunimi:', lname.value);
  // voidaaan tehdä ja heittää nimet flask serverille

});

// Options for retrieving location information (optional)
const options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0,
};

// A function that is called when location information is retrieved
function success(pos) {
  const crd = pos.coords;
  console.log(pos);

  // Printing location information to the console
  console.log('Your current position is:');
  console.log(`Latitude : ${crd.latitude}`);
  console.log(`Longitude: ${crd.longitude}`);
  console.log(`More or less ${crd.accuracy} meters.`);

  // Use the leaflet.js library to show the location on the map (https://leafletjs.com/)
  const map = L.map('map').setView([51.505, -0.09], 13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  L.marker([51.505, -0.09]).
      addTo(map).
      bindPopup('<button>Klikkaa minua, olen tääällä</button>').
      openPopup();
}

// Function to be called if an error occurs while retrieving location information
function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

// Starts the location search
navigator.geolocation.getCurrentPosition(success, error, options);
