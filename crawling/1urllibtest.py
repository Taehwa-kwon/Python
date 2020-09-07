import urllib.request

#해당하는 서버에 요청을 하고 값을 받아오는것 (urllib)

url="https://www.naver.com/"

request = urllib.request.urlopen(url).read()
print(type(request))
print(request.decode('utf-8'))


