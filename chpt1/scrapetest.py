from urllib.request import urlopen
from bs4 import BeautifulSoup

# Tool to Handle Exceptions
from urllib.error import HTTPError

# --- urlopen examle ---
#resp = urlopen('http://pythonscraping.com/pages/page1.html')
#print(resp.read())

# bs4 takes the file object created by urlopen() and 
# can output without needing to html.read() first

url = 'http://taylorcurran.com/'

try:
    resp = urlopen(url)
except HTTPError as e:
    print(e)
else:
    bs = BeautifulSoup(resp, 'html.parser')
    print(bs.h1)

