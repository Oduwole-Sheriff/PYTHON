import requests

payload = {"firstname": "Sheriff", "lastname": "Developer"}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)