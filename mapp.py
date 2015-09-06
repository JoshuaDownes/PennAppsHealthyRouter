import folium

class Mapp:
    clat = None
    clong = None
    bcoord = None
    fcoord = None

    """ Current coordinates, bike station coordinates, farmers market coordinates """
    def __init__(self, clat, clong, bcoord, fcoord, addressFull, bikeFull, foodFull, farmer, bikepath):
        self.clat = clat
        self.clong = clong
        self.bcoord = bcoord
        self.fcoord = fcoord
        self.addressFull = addressFull
        self.bikeFull = bikeFull
        self.foodFull = foodFull
        self.farmer=farmer
        self.cfarm=farmer['geometry']['coordinates']
        self.bikepath=bikepath

    def generateMapp(self):
        map_osm = folium.Map(location=[self.bcoord[1], self.bcoord[0]], width=800, height=500, zoom_start=16)
        map_osm.simple_marker([self.clat, self.clong], popup='You\'re here! '+self.addressFull+"")

        map_osm.circle_marker([self.bcoord[1], self.bcoord[0]], radius=25, popup='Here first, grab a bike! '
                +self.bikeFull['properties']['addressStreet'], fill_color='#0000ff')
        map_osm.circle_marker([self.fcoord[1], self.fcoord[0]], radius=25, 
                popup='Ride here! Pick up something healthy! '+self.foodFull['properties']['STORE_ADDRESS']+
                ', AKA '+self.foodFull['properties']['OFFICIAL_STORE_NAME'], fill_color='#00ff00')
        map_osm.circle_marker([self.farmer['geometry']['coordinates'][1], self.farmer['geometry']['coordinates'][0]], radius=25,
                popup='Ride here for something delicious! '+self.farmer['properties']['ADDRESS']+
                ', AKA '+self.farmer['properties']['NAME']+'. Open '+self.farmer['properties']['TIME']+
                ' during '+self.farmer['properties']['MONTHS'], fill_color='#FFCC00')
        map_osm.line(locations=[[self.clat, self.clong], [self.bcoord[1], self.bcoord[0]], [self.fcoord[1], self.fcoord[0]]])
        map_osm.line(locations=[[self.bcoord[1],self.bcoord[0]], [self.cfarm[1],self.cfarm[0]]])
        for i in range (0,len(self.bikepath['geometry']['coordinates']) - 1):
                map_osm.line(locations=[[self.bikepath['geometry']['coordinates'][i][1], self.bikepath['geometry']['coordinates'][i][0]],
                    [self.bikepath['geometry']['coordinates'][i+1][1], [self.bikepath['geometry']['coordinates'][i+1][0]]]])
        map_osm.create_map(path='templates/mapp.html')



