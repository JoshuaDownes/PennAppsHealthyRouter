from flask import Flask, render_template, request
from flask.ext.mongoengine import MongoEngine
from findNear import * 

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'health_data'}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

@app.route('/', methods=['GET', 'POST'])
def index():
    client = MongoClient()
    db = client.health_data
    collection = db.bike_stations

    compass = findLocation( -75.2, 40 )
    t = compass.nearby(compass.coordinates, collection)
    return render_template("index.html", test=t)

if __name__ == '__main__':
    app.debug = True
    app.run()
