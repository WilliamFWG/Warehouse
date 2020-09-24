import json
from urllib import request

url='http://www.weather.com.cn/data/sk/101010100.html'  #北京的代码101010100
html=request.urlopen(url)
data=html.read()
print(json.loads(data))

