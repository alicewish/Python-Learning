import requests
r = requests.get("http://xlzd.me/query", params={"name":"xlzd", "lang": "python"})
print (r.url)
r = requests.get('http://xlzd.me')
print (r.encoding)
print (r.headers)
print (r.cookies)
print (r.text)