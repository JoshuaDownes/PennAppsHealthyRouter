from pymongo import MongoClient
    
class findLocation:
    coordinates = [0,0]

    def __init__(self, coordinatesx, coordinatesy):
        self.coordinates[0] = coordinatesx
        self.coordinates[1] = coordinatesy

    def nearby(self, coordinates, collection):
        result = None
        for doc in collection.find( { "geometry": { "$near": { "$geometry": { "type": "Point", "coordinates": [coordinates[1], coordinates[0]] } }}}):
            result = doc
            break
        return(result)



