from urllib.request import urlopen
from bs4 import BeautifulSoup

# --- urlopen examle ---
# html = urlopen('http://pythonscraping.com/pages/page1.html')
# print(html.read())

# bs4 takes the file object created by urlopen() and can output
# without needing to html.read() first

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.h1)

