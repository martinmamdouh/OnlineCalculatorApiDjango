import requests
r = requests.post('http://127.0.0.1:7070/api/token/',
                  data={"username": "admin", "password": "EWQ#ewq3"})
print(r.text)
print(r.status_code)
