import folium

class Mapp:
    clat = None
    clong = None
    bcoord = None
    fcoord = None

    """ Current coordinates, bike station coordinates, farmers market coordinates """
    def __init__(self, clat, clong, bcoord, fcoord, addressFull, bikeFull, foodFull):
        self.clat = clat
        self.clong = clong
        self.bcoord = bcoord
        self.fcoord = fcoord
        self.addressFull = addressFull
        self.bikeFull = bikeFull
        self.foodFull = foodFull

    def generateMapp(self):
        map_osm = folium.Map(location=[self.bcoord[1], self.bcoord[0]], width=800, height=500, zoom_start=15)
        map_osm.simple_marker([self.clat, self.clong], popup='You\'re here! '+self.addressFull+"")

        map_osm.circle_marker([self.bcoord[1], self.bcoord[0]], radius=25, popup='Here first! '+self.bikeFull['properties']['addressStreet'], fill_color='#0000ff')
        map_osm.circle_marker([self.fcoord[1], self.fcoord[0]], radius=25, popup='Ride here! '+self.foodFull['properties']['STORE_ADDRESS']+'\n, AKA '+self.foodFull['properties']['OFFICIAL_STORE_NAME'], fill_color='#00ff00')
        map_osm.line(locations=[[self.clat, self.clong], [self.bcoord[1], self.bcoord[0]], [self.fcoord[1], self.fcoord[0]]])
        map_osm.create_map(path='templates/mapp.html')
