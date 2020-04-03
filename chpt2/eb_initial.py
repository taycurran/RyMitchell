from urllib.request import urlopen
from bs4 import BeautifulSoup

url  = 'https://www.eventbrite.com/'

# Automate Method Using Selecotr
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
selector = '#panel0 > div > div:nth-child(1) > div.eds-show-up-sw > div > div.feed-events-bucket__content > div:nth-child(1) > div > div > article > div > div.eds-media-card-content__content > div > div.eds-media-card-content__primary-content > a > h3 > div > div.eds-event-card__formatted-name--is-clamped.eds-event-card__formatted-name--is-clamped-three.eds-text-weight--heavy'
idk = bs.select('#panel0')

print(type(idk))

# RyMitch Way Using Class ? Whatever that is..
element = '<div class="eds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy" aria-hidden="true" role="presentation" data-spec="event-card__formatted-name--content">THIS EVENT IS POSTPONED NEW DATE ANNOUNCED SOON. TICKET HOLDERS PLEASE CHEC...</div>'
class_ = 'ds-event-card__formatted-name--is-clamped eds-event-card__formatted-name--is-clamped-three eds-text-weight--heavy'
idk2 = bs.find_all(class_=class_)
# Its Not Working

print(idk2)

# WHERE DO SELECTORS COME IN?
