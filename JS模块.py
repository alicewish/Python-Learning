import json

js = json.loads('{"insun": "泰囧 / 人在囧途2 / Lost in Thailand "}')
print(json.dumps(js))
print(json.dumps(js, ensure_ascii=False))
