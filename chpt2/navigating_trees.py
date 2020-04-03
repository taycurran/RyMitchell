"""
The find_all() method is responsible for finding tags 
based on their name and attributes..
But what if you need to find a tag based on its location in a document?
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://pythonscraping.com/pages/page3.html'

html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')

# Find Children
print('CHILDREN')
for child in bs.find('table', {'id':'giftList'}).children:
    print(child)

# Find Siblings
# The output of this code is to print all rows of products from the product table,
# except for the first title row as objects cannot be siblings with themselves.
# Siblings are on parallel (same levels) of the tree
print("SIBLINGS")
for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

print('PARENTS')
print(bs.find('img',
            {'src':'../img/gifts/img1.jpg'})
            .parent.previous_sibling.get_text())