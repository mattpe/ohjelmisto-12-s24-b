from flask import Flask, Response, render_template
import json
import alkulukulaskuri

app = Flask(__name__)

@app.route('/')
def moikka():
    return 'Alkulukutehtävä'

@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    try:
        luku1 = float(luku1)
        luku2 = float(luku2)
        summa = luku1+luku2

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku1": luku1,
            "luku2": luku2,
            "summa": summa
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

# http://127.0.0.1:3000/alkuluku/31
@app.route('/alkuluku/<alkuluku>')
def alkuluku(alkuluku):
    try:
        luku = int(alkuluku)
        # laske tässä alkuluku TAI kutsu funktiota toisesta tiedostosta
        alkuluku = alkulukulaskuri.laske(luku)

        tilakoodi = 200

        vastaus = {
            "Number": luku,
            "isPrime": alkuluku
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku alkulukua ei voida laskea"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

# http://127.0.0.1:3000/kentta/EFHK
@app.route('/kentta/<icao>')
def haekenttä(icao):
    try:
        # hae tässä icaon avulla mariadb päällä tietokannasta oikea kaupunki

        tilakoodi = 200
        vastaus = {
            "ICAO":"EFHK",
            "Name":"Helsinki Vantaa Airport",
            "Municipality":"Helsinki"
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": ""
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")



@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    #return Response(response=jsonvast, status=404, mimetype="application/json")
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)