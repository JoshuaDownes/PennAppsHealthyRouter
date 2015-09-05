import folium

class Mapp:
    clat = None
    clong = None
    bcoord = None
    fcoord = None

    """ Current coordinates, bike station coordinates, farmers market coordinates """
    def __init__(self, clat, clong, bcoord, fcoord):
        self.clat = clat
        self.clong = clong
        self.bcoord = bcoord
        self.fcoord = fcoord

    def generateMapp(self):
        map_osm = folium.Map(location=[self.bcoord[1], self.bcoord[0]], width=500, height=400, zoom_start=15)
        map_osm.simple_marker([self.clat, self.clong], popup='You\'re here!')

        map_osm.circle_marker([self.bcoord[1], self.bcoord[0]], radius=25, popup='Bike Station: Walk here!', fill_color='#ff0000')
        map_osm.circle_marker([self.fcoord[1], self.fcoord[0]], radius=25, popup='Fresh and Delicious Food: Ride here!', fill_color='#0000ff')
        map_osm.create_map(path='templates/mapp.html')
