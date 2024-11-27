'use strict';
  document.querySelector('form').addEventListener('submit', function(evt) {
    console.log(evt);
    evt.preventDefault();
    const searchW = document.getElementById('query').value;
    console.log(searchW);
    getTvShows(searchW);
  });

  async function getTvShows(searchW) {
    // palauttaa response objektin joka on promise, tehdään asynkronisesti
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${searchW}`);
    console.log(response);
    // muuntaa vastauksen datan json muotoon
    // on myös promise sillä tämäkin tehdään asynkronisesti
    const data = await response.json();
    createArticles(data);
  }

  function createArticles(data) {

    document.getElementById('results').innerHTML = '';
    console.log(data);

    for (const movie of data) {
      console.log(movie.show.name);

      const article = document.createElement('article');

      const h2 = document.createElement('h2');
      h2.innerText = movie.show.name;

      const link = document.createElement('a');
      link.innerText = movie.show.url;
      link.href = movie.show.url;
      link.target = '_blank';

      const img = document.createElement('img');
      img.alt = movie.show.name;
      // img.src = movie.show.image?.medium || 'https://placedog.net/210/230';

      //
      // if (movie.show.image ) {
      //  img.src = movie.show.image.medium;
      // } else {
      //  img.src = 'https://placedog.net/210/230';
      //}

      // ehto
      // ? arvoJosOnTrue
      // : arvoJosOnFalse;

      img.src = movie.show.image ? movie.show.image.medium : 'https://placedog.net/210/230';

      const div = document.createElement('div');
      div.innerHTML = movie.show.summary;

      article.appendChild(h2);
      article.appendChild(link);
      article.appendChild(img);
      article.appendChild(div);

      document.getElementById('results').appendChild(article);

    }
  }

  /*

    <article>
      <h2>name</h2>
      <a href="url" target="_blank">url</a>
      <img src="medium-image" alt="name"/>
      <div>summary</div>
    </article>

*/
  /*
  async function getTvShows2(searchW) {
    try {
      const response = await fetch(`https://api.tvmaze.com/search/shows?q=${searchW}`);
      console.log(response);
      if (!response.ok) {
        throw new Error(response.status.toString());
      }
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  }*/