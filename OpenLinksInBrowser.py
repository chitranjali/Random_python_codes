#! /usr/bin/env
from sys import argv
from bs4 import BeautifulSoup
import requests
import webbrowser

search_phrase = ' '.join(argv[1:])
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + search_phrase)
res.raise_for_status()

res_soup = BeautifulSoup(res.text,'html.parser')
# Get all search result links which are in class 'r' as list
linkElems = res_soup.select('.r a')

# Open 5 or less than that links in browser
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))




