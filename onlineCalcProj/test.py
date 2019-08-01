import re
from math import *

if re.match("[-+\*\/e 0-9]+$", 'ee-6+6*5'):
    print('yes')
else:
    print('no')

lis = [5+2+3, 2+1, 2*(7-3)]
for s in lis:
    x = eval(str(s))
    print(x, 'ss', sqrt(x))


def cubeRoot(num):
    if 0 <= num:
        return num**(1./3.)
    return -(-num)**(1./3.)


def factorial(num):
    """This is a recursive function that calls
   itself to find the factorial of given number"""
    if num in[1, 0, -1]:
        return num

    elif num > 1:
        return num * factorial(num - 1)
    else:
        num = abs(num)
        return -(num * factorial(num - 1))


print(eval('[math.cosh(5)]',
           {'__builtins__': None}, {'pow': pow, 'sqrt': sqrt, 'cubeRoot': cubeRoot, 'factorial': factorial,
                                    'cos': cos, 'sin': sin, 'pi': 3.741
                                    }))
print(cos(50))
