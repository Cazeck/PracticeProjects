import requests
from bs4 import BeautifulSoup

# Request information from Website
r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

# Pull data from request (HTML)
c = r.content

soup = BeautifulSoup(c, "html.parser")

# List of all divs from the html
all = soup.find_all("div", {"class": "cities"})

print(all)

# Print each City name from the h2 section
for item in all:
    print(item.find_all("h2")[0].text)

