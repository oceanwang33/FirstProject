
from bs4 import BeautifulSoup

myHtml='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>this is my title</title>
</head>
<body>
<h1>第一个测试</h1>
<h1>这是第二个h1</h1>
<h2>love</h2>
<h3>this is h3.</h3>
<p>这是海洋，我喜欢你们。是的</p>
</body>
</html>'''

soup=BeautifulSoup(myHtml,'html.parser')

myH1=soup.find('h1')
myH1All=soup.findAll('h1')
print(myH1)
print(myH1.string)

print(myH1All)
for i in myH1All:
    print(i.string)

for i in myH1All:
    if '这是' in i.string:
        print(i.string)




