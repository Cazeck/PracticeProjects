"""
Folium makes maps by turning python code into html and javascript
"""
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

# Creates base layer map
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

# Can add multiple features within this FeatureGroup such as map markers
fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

# Now we can add all of our features to the map at once
map.add_child(fg)

map.save("Map1.html")



