from bs4  import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import requests

url = "www.pythonforbeginners.com"

r = requests.get("http://"+ url)

data = r.text

soup = BeautifulSoup(data,"lxml")
print (soup.head.title.string)
