import requests

def search_show(search_term):
    # HTTP GET https://api.tvmaze.com/search/shows?q=emmerdale
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    # Käsitellään mahdolliset virheet verkkoyhteydessä.
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe!")
        # print(e)
        return

    # testataan, että http status koodi OK, muuten lopetetaan suoritus tähän
    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}")
        return

    # Parsitaan json datasta Pythonin tietorakenne (lista jonka sisällä sanakirjoja ja listoja)
    response_body = response.json()

    if len(response_body) < 1:
        print("Ei tuloksia.")
        return

    # Näytetään vain ensimmäisen hakutuloksen nimi
    #print(response_body[0]['show']['name'])

    # iteroidaan response body (http-vastauksen runko) silmukalla
    print("Kaikki Hakutulokset\n------------")
    for item in response_body:
        print(item['show']['name'])
        print(f"TV-ohjelman tyyppi: {item['show']['type']}")
        for genre in item['show']['genres']:
            print(genre)
        print("---")

# search_show("emmerdale")
search_show(input("Anna TV-hakusana: "))
