import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

# Creates base layer map
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Can add multiple features within this FeatureGroup such as map markers
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev): # zip iterates through multiple lists simultaneously
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color='green')))

# Now we can add all of our features to the map at once
map.add_child(fg)

map.save("Map1.html")

