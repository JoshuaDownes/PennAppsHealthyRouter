from pymongo import MongoClient

"""WIP -- Not implemented yet"""

class BikePathFinder:
    nodes = None
    source = None
    dest = None
    client = MongoClient()
    db = client.health_data 
    collection = db.bike_network

    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        for doc in collection:
            for geo in doc['geometry']:
                for coords in geo['coordinates']:
                    nodes.append(coords)

    def findBikePath():
        visited = [self.source]
        unvisited = self.nodes.append[self.dest]
        while self.dest not in visited:




    """ Distance will be defined as the greater of horizontal or vertical distance to avoid diagonal travel through buildings """
    """ TEST DISTANCE FUNCTION CUBED """
    def calcDistance(x1, y1, x2, y2):
        if abs(x1-x2) > abs(y1-y2):
            return abs(x1-x2)
        return abs(y1-y2)



