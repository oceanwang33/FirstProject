
from bs4 import BeautifulSoup
import requests

data=requests.get('https://www.baidu.com').content

soup=BeautifulSoup(data,'html.parser')

print(soup.title.text)

print(soup.body.div.attrs)

