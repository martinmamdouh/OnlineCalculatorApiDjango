import requests
r = requests.post('http://127.0.0.1:7070/api/token/',
                  data={"username": "user", "password": "megasoft123"})
print(r.text)
print(r.status_code)
print(r.json())