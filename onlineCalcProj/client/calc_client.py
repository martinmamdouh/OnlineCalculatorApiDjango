import requests
import urllib.parse
from configuration import ApiConfig
def get():
       expression=urllib.parse.quote('[5/6]',safe='')
       res=requests.get(f'http://127.0.0.1:7070/megasoft/api/v1.0/calculate/?expression={expression}',
       headers=ApiConfig.headers)
       print(res.text)

def post():
       res=requests.post('http://127.0.0.1:7070/megasoft/api/v1.0/calculate/',
       headers=ApiConfig.headers,
       data={'expression':['pow(tan(2),2)','(8)+(8*2)+pow(((8+2)+1),2)','tan(2*pi)-5-2*tan(2*pow((pi),2))','pow(4+2,3)/2+sqrt(2)','5+6*2/8']})
       print(res.text)
get()
post()