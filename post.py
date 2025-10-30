import requests
x = requests.get("https://reqres.in/api/users")
print(x.status_code)
print(x.json())