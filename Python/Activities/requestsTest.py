import requests
print(requests.get('https://training-support.net'))
r = requests.get('https://www.python.org')
print(r.status_code)