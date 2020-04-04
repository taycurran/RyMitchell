from urllib.request import urlopen
from bs4 import BeautifulSoup

# Import Regular Expressions
# Import Regular Expression Capability
import re

url = 'http://pythonscraping.com/pages/page3.html'

html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')

# Without Regular Expressions
images = bs.find_all('img')
print('SANS REGEX')
for image in images:
    print(image['src'])

# With Regex
images = bs.find_all('img',
    {'src':re.compile('..\/img\/gifts/img.*.jpg')}
)

print('WITH REGEX')
for image in images:
    print(image['src'])