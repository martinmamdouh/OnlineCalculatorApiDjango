from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from .calculator import Calculator
from .serializer import CalculatorResponseSerializer,CalculatorPostSerializer
from rest_framework.views import APIView
from operationsHistory.models import History
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .swaggerSchema import SimpleFilterBackend


class OnlineCalculator(GenericAPIView):
       permission_classes = [IsAuthenticated]
       filter_backends = (SimpleFilterBackend,)
       
       #override swagger get_serializer_class serializer
       def get_serializer_class(self,*args,**kwargs):

              if self.request.method == 'POST':
                     return CalculatorPostSerializer
              return CalculatorResponseSerializer


       def __init__(self):
              self.__expression=None
              self.__result=None
              

       def __useCalculator(self):
              calculator=Calculator()
              print(self.__expression)
              self.__expression=str(self.__expression).replace('\'','').replace('\"','')
              print(self.__expression)
              result=calculator.calculate(self.__expression)
              return result

       def __getSerializedResult(self):

              calculatorResponseSerializer=CalculatorResponseSerializer(data=self.__result)
              if calculatorResponseSerializer.is_valid(): 
                    return calculatorResponseSerializer.data
              else:
                     return calculatorResponseSerializer.errors

       def __saveHistory(self):

              opsHistory=History(
                     expression=self.__expression,
                     ans=self.__result['ans'],
                     error=self.__result['error']
              )
              opsHistory.save()


       def get(self,request ,format=None):
              
              '''
              ?expression=[5*2,12/4] 
              --The expression must be url encoded.
              --The expression must be list of string.
              '''
              #get expression from URL 
              self.__expression=request.GET.get('expression',['invalid'])
              self.__result=self.__useCalculator()
              data=self.__getSerializedResult()
              self.__saveHistory()
              if self.__result['ans']:
                     status=200
              else:
                     status=400
              return JsonResponse(data, status=status)

       def post(self,request ,format=None):
              '''
              
              --The expression must be list of string.

              { 'expression':
                     [ '5+2',
                     '5+6*2/8',
                     'factorial(5)',
                     'pow(10,2)',
                     'tan(2*pi)',
                     'pow(4+2,3)/sqrt(9)' ]
              }
              '''
              
              calculatorPostSerializer=CalculatorPostSerializer(data=request.data)
              if calculatorPostSerializer.is_valid(): 
                     self.__expression=calculatorPostSerializer.data['expression']
                     self.__result=self.__useCalculator()
                     data=self.__getSerializedResult()
                     self.__saveHistory()
                     
                     if self.__result['ans']:
                            status=200
                     else:
                            status=400
                     return JsonResponse(data,status=status)

              return JsonResponse(calculatorPostSerializer.errors,status=400)
