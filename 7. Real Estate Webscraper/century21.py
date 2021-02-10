import requests
import pandas
from bs4 import BeautifulSoup

# Cached version of website: http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/
r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")

# Finding out what is the total number of pages we need to scrape through
page_nr = soup.find_all("a", {"class": "Page"})[-1].text

l = []

# Base link we can edit the last value to change webpages
base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="

# Iterating through all webpages for these listings
for page in range(0, int(page_nr)*10, 10):
    r = requests.get(base_url + str(page), headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    # Pull each of the propertyRow divs from the HTML
    all = soup.find_all("div", {"class": "propertyRow"})

    # Looping through the propertyRows and extracting data
    # Will add all values into a list of dictionaries in order to store
    for item in all:
        d = {}
        # Address
        d["Address"] = item.find_all("span", {"class": "propAddressCollapse"})[0].text

        # City
        try:
            d["Locality"] = item.find_all("span", {"class": "propAddressCollapse"})[1].text
        except:
            d["Locality"] = None

        # Price
        d["Price"] = item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")

        # Num of Beds
        try:
            d["Beds"] = item.find("span", {"class": "infoBed"}).find("b").text  # Sometimes this is a None type
        except:
            d["Beds"] = None           # For consistent formatting when we have all of the values

        # Num of SqFt
        try:
            d["Area"] = item.find("span", {"class": "infoSqFt"}).find("b").text
        except:
            d["Area"] = None

        # Num of Baths
        try:
            d["Full Baths"] = item.find("span", {"class": "infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None

        # Num of Half Baths
        try:
            d["Half Baths"] = item.find("span", {"class": "infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None

        # Pulling "Lot Size" from the Features section
        for column_group in item.find_all("div", {"class": "columnGroup"}):
            # Iterating through both of these sections at the same time using zip
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        l.append(d)

# Make pandas DataFrame
df = pandas.DataFrame(l)
df.to_csv("Output.csv")