import urllib.request
from bs4 import BeautifulSoup

wellington_url = "http://wellington.dns-systems.net/pages/beerboard.php"

def getHTML(url):
    contents = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(contents, 'html.parser')
    return soup

bear_list = []
for bear in getHTML(wellington_url).find_all('tr'):
    bear_list.append(bear)
bear_list.pop(0)

print("-- The Wellington --")
for i in range(0, len(bear_list)):
    name = bear_list[i].find_all('td')[2].getText().strip()
    price = str(bear_list[i].find_all('td')[4].getText()).replace(" ", "")
    print("> " + name + ", " + price )
