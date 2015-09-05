from flask import Flask, render_template, request
from pymongo import MongoClient
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
    
    form = AddressForm(request.form)
    if request.method == 'POST':
        """ Find closest bike station to given address """
        collection = db.bike_stations
        addr = request.form.get("address")
        geolocator = OpenCage('d79317ac2c4be89c2683778d8a95df49')
        location = geolocator.geocode(addr)
        compass = findLocation( location.latitude, location.longitude)
        closestBikeStation = compass.nearby(compass.coordinates, collection)

        """ Switch to finding closest farmer's market to bike station """
        compass = findLocation( closestBikeStation['geometry']['coordinates'][0], closestBikeStation['geometry']['coordinates'][1] )
        collection = db.farmers_markets
        closestFarmersMarket = compass.nearby(compass.coordinates, collection)

        """ Return new page with found values plugged into template """
        return render_template("result.html", bikestation=closestBikeStation['properties']['addressStreet'],
                farmersmarket=closestFarmersMarket['properties']['ADDRESS'])
    else:
        return render_template("index.html", form=form)

@app.route('/hroute', methods=['GET', 'POST'])
def hroute():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()
