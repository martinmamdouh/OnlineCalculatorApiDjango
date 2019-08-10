import requests
import urllib.parse
from configuration import ApiConfig

def get():
       expression=urllib.parse.quote('[5+6]')
       res=requests.get(f'{ApiConfig.hostname}/megasoft/api/v1.0/calculate/?expression={expression}',
       headers=ApiConfig.headers)
       print(res.text)
       print(res.status_code)

def post():
       res=requests.post(ApiConfig.hostname+'/megasoft/api/v1.0/calculate/',
       headers=ApiConfig.headers,
       data={'expression':[
       'factorial(512.0)','pow(tan(2),2)','tan(2*pi)-5-2*tan(2*pow((pi),2))','pow(4+2,3)/2+sqrt(2)','5+6*2/8']})
       print(res.text)
       print(res.status_code)
get()
post()