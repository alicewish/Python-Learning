import json, requests

obj = [[1, 2, 3], 123, 123.123, 'abc', {'key1': (1, 2, 3), 'key2': (4, 5, 6)}]
encodedjson = json.dumps(obj)
print(repr(obj))
print(encodedjson)

html = requests.get('http://api.kanzhihu.com/userdetail2/97eda4b3357310f333d6c493f748d165')
encodedhtml = json.dumps(html)
print(repr(html))
print(encodedhtml)
#todo