# Ohjelmisto 1 kurssin koodiesimerkit

Opettajien github-tunnukset: UllaSe ja mattpe

## `if-else` vs. `while` control flow

If:

```mermaid
graph TD;
    A[Start] --> B{Condition?};
    B -->|True| C[Execute If-Block];
    B -->|False| D[Execute Else-Block];
    C --> E[End];
    D --> E[End];
```

If & else-if (elif):

```mermaid
graph TD;
    A[Start] --> B{Condition 1?};
    B -->|True| C[Execute If-Block];
    B -->|False| D{Condition 2?};
    D -->|True| E[Execute Elif-Block];
    D -->|False| F[Execute Else-Block];
    C --> G[End];
    E --> G[End];
    F --> G[End];
```

While:

```mermaid
graph TD;
    A[Start] --> B{Condition?};
    B -->|True| C[Execute Loop Body];
    C --> B;
    B -->|False| E[End];
```

## Tips

Vinkkejä mahdollisiin ongelmatilanteisiin GitHubin kanssa.

Jos virheilmoitus valittaa, että tunnus/käyttäjänimi puuttuu, aseta ne terminaalissa:

```sh
git config --global user.email "sinun.maili@osoitteesi.fi"
git config --global user.name "Sinun Nimesi"
```

Sähköpostiosoitteen pitää olla sama, mitä käytit GitHubiin rekisteröityessäsi.

Repon luominen Githubissa onnistuu, mutta ei oikeuksia/push ei onnistu: 

- Tarkista terminaalissa komennolla `git remote -v`:
  - origin osoitteen pitää alkaa `https://...`
  - osoitteen pitää loppua `repon-nimi.git`, jossa `repon-nimi` sama kuin projektin nimi githubissa

