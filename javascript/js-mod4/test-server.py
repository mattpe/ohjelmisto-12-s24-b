from flask import Flask
# Asenna Flask Cors paketti ensin
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/airport/<icao>')
def airport(icao):
  # add database query here
  return {'ICAO': icao, 'Name': 'Airport name'}

app.run()