'use strict';
console.log('script start');


async function fetchImages() {
    const response = await fetch('pics.json');
    console.log('pic response', response);
    // jos vastaus ok (eli statuskoodi 2xx)
    if (response.ok) {
        const pics = await response.json();
        console.log('kuvat:', pics)
        for (const pic of pics) {
            const imgElem = document.createElement('img');
            imgElem.src = pic.address;
            imgElem.alt = pic.description;
            document.querySelector('#images').append(imgElem);
        }
    }
}
fetchImages();

// Chuck norris api esimerkki
async function getAJoke() {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const joke = await response.json();
    console.log('vitsi: ', joke.value);
    document.querySelector('#joke').textContent = joke.value;
}
// haetaan vitsi vain käyttäjän pyynnöstä
document.querySelector('#get-joke')
    .addEventListener('click', getAJoke);


document.querySelector('#joke').textContent = "odotetaan vieläkin";
console.log('script end');
