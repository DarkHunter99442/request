import requests
x=requests.get("https://jsonplaceholder.typicode.com/posts")
print(x.status_code)
print(x.text)
with open("new.json","w") as p:
    p.write(x.text)
