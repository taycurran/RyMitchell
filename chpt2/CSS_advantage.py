from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/warandpeace.html'

# HTML File Object
resp = urlopen(url)
# Beautiful Soup Object
bs = BeautifulSoup(resp.read(), 'html.parser')

nameList = bs.find_all('span', {'class':'green'})

for name in nameList:
    print(name.get_text())

princeList = bs.find_all(text='the prince')
print(len(princeList))


