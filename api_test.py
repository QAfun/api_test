import requests

res = requests.get('http://ip-api.com/json')

data = res.json()
print(data.get('country'))
print(data.get('query', 'not found'))
print(data.get('test', 'not found'))
print(data)
