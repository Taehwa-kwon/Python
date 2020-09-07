import requests

url = 'http://127.0.0.1:80/list'

res = requests.get(url)
print(res.text)