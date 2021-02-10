import requests
from bs4 import BeautifulSoup

# Cached version of website: http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/
r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

soup = BeautifulSoup(c, "html.parser")

# Pull each of the propertyRow divs from the HTML
all = soup.find_all("div", {"class": "propertyRow"})

# Looping through the propertyRows and extracting data
for item in all:
    # Price
    print(item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", ""))
    # Address
    print(item.find_all("span", {"class": "propAddressCollapse"})[0].text)
    # City
    print(item.find_all("span", {"class": "propAddressCollapse"})[1].text)
    # Num of Beds
    try:
        print(item.find("span", {"class": "infoBed"}).find("b").text)  # Sometimes this is a None type
    except:
        print(None)             # For consistent formatting when we have all of the values

    # Num of SqFt
    try:
        print(item.find("span", {"class": "infoSqFt"}).find("b").text)
    except:
        print(None)

    # Num of Baths
    try:
        print(item.find("span", {"class": "infoValueFullBath"}).find("b").text)
    except:
        print(None)

    # Num of Half Baths
    try:
        print(item.find("span", {"class": "infoValueHalfBath"}).find("b").text)
    except:
        print(None)

    print(" ")