import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'

res = urllib.request.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
print(soup.prettify())

result1 = soup.select('p.title>a')
result2 = soup.select('p.artist>a')
result3 = soup.select('td>a.album')

title = []
artist = []
album = []

for re in result1 :
    #print(re.string)
    title.append(re.text)

for re in result2 :
    #print(re.string)
    artist.append(re.text)

for re in result3 :
    #print(re.string)
    album.append(re.text)

ziplist = list(zip(title, artist, album))
#print(ziplist)


import json

f = open('crawling/ziplist.json', 'wt')
json.dump(ziplist, f)
f.close()

f = open('crawling/ziplist.json', 'rt')
data = json.load(f)
#print(data)