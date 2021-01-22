import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

# Change the markers color depending on elevation height
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return 'red'

# Creates base layer map
map = folium.Map(location=[38.58,-99.09], zoom_start=5, tiles="Stamen Terrain")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Can add multiple features within this FeatureGroup such as map markers
fgv = folium.FeatureGroup(name="Volcanoes")

# zip iterates through multiple lists simultaneously
for lt, ln, el in zip(lat, lon, elev):
    # Adding volcano markers
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m", fill_color=color_producer(el),
                                     color="black", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

# Now we can add all of our features to the map at once
# our 3rd polygon layer for the map, has information such as the coordinates for country boarders
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Now we can add all of our features to the map at once
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")

