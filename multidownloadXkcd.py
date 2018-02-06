from bs4 import BeautifulSoup
import requests,sys,os,threading

# Downloading XKCD comics with threading
os.makedirs('xkcd', exist_ok=True)  # Create DIR to Store comics in ./xkcd in CWD
url = 'https://xkcd.com'

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        url = 'https://xkcd.com' + '/' + str(urlNumber) + '/'
        comic_page = requests.get(url)
        comic_page.raise_for_status()
        comic_soup = BeautifulSoup(comic_page.text, 'html.parser')

        image = comic_soup.find('div', id='comic')
        comic = image.find("img")
        print(comic["src"])

        comicUrl = 'http:' + comic["src"]
        try:
            res = requests.get(comicUrl)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        # res.raise_for_status()

        # Open an image file and write image as chunks of  100k bytes
        imageFile = open(os.path.join('xkcd1', os.path.basename(comicUrl)), 'wb')
        # imageFile = open(os.path.join('xkcd1', str(urlNumber) + '.png'), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

# This to check the last comic number!!
print('Downloading page %s...' % url)
comic_page = requests.get(url)
comic_page.raise_for_status()
comic_soup = BeautifulSoup(comic_page.text, 'html.parser')

# Get the Prev button's url.
prev = comic_soup.find('ul', {"class": "comicNav"})
prev_link = prev.find('a', href=True, rel="prev")
url = 'https://xkcd.com' + prev_link["href"]
total = prev_link["href"].strip('/')

downloadThreads = []
Total_comics = int(total) + 2 #Add 1 for latest one and one for using in range!

for i in range(1, Total_comics, 100):

    # endComic till the total number of comics!
    endComic = i + 99
    if endComic > Total_comics:
        endComic = Total_comics
    # Create threads with intervals...
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, endComic))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Print Done only after all threads are closed
for downloadThread in downloadThreads:
    downloadThread.join()
print(" Downloaded all comics")