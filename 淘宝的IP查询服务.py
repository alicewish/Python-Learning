import requests

url = 'http://ip.taobao.com/service/getIpInfo.php'
payload = {'ip': '23.91.98.188'}
r = requests.get(url, params = payload)
print(r.json()['data']['country_id'])