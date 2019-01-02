
from bs4 import BeautifulSoup
import requests

baidu=requests.get('https://www.baidu.com').content

soup=BeautifulSoup(baidu,'html.parser')
print(soup.text)
print('-------------------------------------------------------------------------------')

links=soup.findAll('a')     # <a>是html中的的链接部分
print(links)
print('-------------------------------------------------------------------------------')

for link in links:
    print(link)
print('-------------------------------------------------------------------------------')

for link in links:
    print(link.string)
print('-------------------------------------------------------------------------------')

