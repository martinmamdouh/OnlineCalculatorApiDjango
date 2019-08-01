
from calculator import Caclulator

c=Caclulator()
result=c.calculate('[5+5,tan(5510)]')
if result.error:
       print('error ',result.error)
else:
       print(result.ans)