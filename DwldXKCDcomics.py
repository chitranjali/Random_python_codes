from bs4 import BeautifulSoup
import requests
import os

os.makedirs('xkcd', exist_ok=True)  #Create DIR to Store comics in ./xkcd

url = 'https://xkcd.com'

while url:
    print('Downloading page %s...' % url)
    comic_page = requests.get(url)
    comic_page.raise_for_status()
    comic_soup = BeautifulSoup(comic_page.text, 'html.parser')

    image = comic_soup.find('div', id='comic')
    comic = image.find("img")
    print(comic["src"])

    comicUrl = 'http:' + comic["src"]
    res = requests.get(comicUrl)
    res.raise_for_status()

    # Open an image file and write image as chunks of  100k bytes
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url.
    prev = comic_soup.find('ul', {"class": "comicNav"})
    prev_link = prev.find('a', href=True, rel="prev")
    url = 'https://xkcd.com' + prev_link["href"]

print(" Downloaded all comics")
