import requests
x= requests.post('https://httpbin.org/post', data={'new': 'value'})
print(x.status_code)
print(x.json())
with open("black.text","w") as f:
    f.write(x.text)
