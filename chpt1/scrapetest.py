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

# Example of Error Handling

def getTitle(url):
    try:
        resp = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(resp.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle(url)
if title == None:
    print('Title could not be found.')
else:
    print(title)
