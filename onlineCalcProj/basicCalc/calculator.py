import re
from math import pow,sqrt,sin,cos,tan,sinh,cosh,tanh 
#from functools import reduce
# Result Object Interface


class Calculator:

       
       def __cubeRoot(self,num):
              if 0 <= num:
                  return num**(1./3.)
              return -(-num)**(1./3.)

       def __factorial(self,num):
              
               if num in[1, 0, -1]:
                   return num

               elif num > 1:
                   return num * self.__factorial(num - 1)
               else:
                   num = abs(num)
                   return -(num * self.__factorial(num - 1))
                   
       def __evaluate(self,expression):
              
              return eval(str(expression),
                     {'__builtins__': None},
                     {      
                            'pow': pow,
                            'sqrt': sqrt,
                            'cubrt': self.__cubeRoot,
                            'factorial': self.__factorial,
                            'cos': cos, 
                            'sin': sin,
                            'tan': tan, 
                            'pi': 3.141592653589793238462643383279502884197169399
                     })
            
       def calculate(self,expression):
              ans=None
              error=None
              try:
                     ans=self.__evaluate(expression)
              except Exception as err:
                     print(err)
                     error='Invalid Expression'
              finally:
                     result={'ans':ans,'error':error}
                     return result




