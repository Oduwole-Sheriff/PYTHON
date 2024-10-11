import requests

payload = {"firstName": "John", "lastName":"Smith" }
r = requests.get("https://httpbin.org/get", params=payload)
print(r.url)
print(r.content)
print(r.text)

payload = {"firstName": "John", "lastName":"Smith" }
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

url = "https://httpbin.org/cookies"

cookies = {'location': 'New York'}
r = requests.get(url, cookies=cookies)
print(r.text)

r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)

s = requests.Session()
userName = {'userName': "John99"}
location = {'location': 'NewYork'}

setCookieUrl = 'https://httpbin.org/cookies/set'
getCookiesUrl = "https://httpbin.org/cookies"

s.get(setCookieUrl, params=userName)
s.get(setCookieUrl, params=location)

r = s.get(getCookiesUrl)
print(r.text)

def response_info(r, *args, **kwargs):
    print(r.status_code, r.url)
    print(r.text)

def response_headers(r, *args, **kwargs):
    print(r.headers)

hooks = {'response': response_info}
r = requests.get('https://httpbin.org/get', hooks=hooks)



























    
