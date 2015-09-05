from flask import Flask, render_template, request
from flask.ext.mongoengine import MongoEngine
from geopy.geocoders import OpenCage
from findNear import * 
from addressForm import *

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
    
    form = AddressForm(request.form)
    if request.method == 'POST':
        addr = request.form.get("address")
        geolocator = OpenCage('d79317ac2c4be89c2683778d8a95df49')
        location = geolocator.geocode(addr)
        return render_template("index.html", test=location.latitude, form=form)
    else:
        return render_template("index.html", form=form)

if __name__ == '__main__':
    app.debug = True
    app.run()
