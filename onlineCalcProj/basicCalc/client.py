import requests
import urllib.parse

def get():
       expression=urllib.parse.quote('[5/6]',safe='')
       res=requests.get(f'http://127.0.0.1:7070/megasoft/api/v1.0/calculate/?expression={expression}')
       print(res.text)

def post():
       res=requests.post('http://127.0.0.1:7070/megasoft/api/v1.0/calculate/',
       data={'expression':['factorial(5)*pow(5,2)','sin(2*pi)','5+6*2/8']})
       print(res.text)
get()
post()