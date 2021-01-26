import urllib.request
from bs4 import BeautifulSoup
import html5lib


wiki = 'https://www.youtube.com/c/AcademiaFernandinhoBeltr%C3%A3o/videos'
page = urllib.request.urlopen(wiki)
soup =  BeautifulSoup(page, 'html5lib')
all_links = soup.find_all('a')

for link in all_links:
    print(link.get('href'))