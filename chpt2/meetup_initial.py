from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import requests

url = 'https://www.meetup.com/find/us--ny--new-york/tech'
r = requests.get(url)
resp = r.encoding

url = 'https://www.meetup.com/find/us--ny--new-york/tech'

# html = urlopen(url)
bs = BeautifulSoup(resp, 'html.parser')

print(bs.prettify())