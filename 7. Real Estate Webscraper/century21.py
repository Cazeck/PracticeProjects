import requests
from bs4 import BeautifulSoup

# Cached version of website: http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/
r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

soup = BeautifulSoup(c, "html.parser")

# Pull each of the propertyRow divs from the HTML
all = soup.find_all("div", {"class": "propertyRow"})

# Pulling the Price of a property from a row
print(all[0].find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", ""))