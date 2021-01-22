import pandas
import geopy
from geopy.geocoders import ArcGIS

nom = ArcGIS()

df = pandas.read_csv("supermarkets/supermarkets.csv")

# Turns n into a location object for the specified address
n = nom.geocode("3995 23rd St, San Francisco, CA 94114")

# Combines info into a new Address Column
df["Address"]=df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

# Applying the geocode method to all addresses in the table
df["Coordinates"] = df["Address"].apply(nom.geocode)

print(df)
print(df["Coordinates"])

# Adding Latitude and Longitude Columns (Lambda is to apply the function to each value)
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)

print(df)