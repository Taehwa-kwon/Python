import requests
url = 'http://127.0.0.1:80/updateprocess'
values = {
    'name' : '권태화',
    'email' : 'taehwa@gmail.com',
    'address' : '거제시'
}

res = requests.post(url,data=values)  #장점은 여기부분
print(res.url)
print(res.next)