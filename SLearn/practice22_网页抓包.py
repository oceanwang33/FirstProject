#windows下安装requests包：pip install requests
#windows下更新pip：python -m pip install --upgrade pip
#windows下更新pip：python -m pip install -U pip
#windows下查pip版本：pip --version
#windows下卸载pip：python -m pip uninstall pip

import requests
text=requests.get('https://news.baidu.com/')
print(text.content)