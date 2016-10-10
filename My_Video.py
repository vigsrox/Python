from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

import requests

url = "http://www.youtube.com"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data,'html.parser')

for link in soup.find_all('a'):
    print (url+(link.get('href')))


        





