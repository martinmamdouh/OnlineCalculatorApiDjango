from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .calculator import Calculator
from .serializer import CalculatorResponseSerializer,CalculatorPostSerializer
from rest_framework.views import APIView

class OnlineCalculator(APIView):

       def __useCalculator(self,expression):
              calculator=Calculator()
              expression=str(expression).replace('\'','').replace('\"','')
              result=calculator.calculate(expression)
              return result

       def __getSerializedResult(self,result):

              calculatorResponseSerializer=CalculatorResponseSerializer(data=result)
              if calculatorResponseSerializer.is_valid(): 
                    return calculatorResponseSerializer.data
              else:
                     return calculatorResponseSerializer.errors

       def get(self,request ,format=None):
              expression=request.GET.get('expression',['0'])
              result=self.__useCalculator(expression)
              serializer=self.__getSerializedResult(result)
              return JsonResponse(serializer)

       def post(self,request ,format=None):

              calculatorPostSerializer=CalculatorPostSerializer(data=request.data)
              if calculatorPostSerializer.is_valid(): 
                     expression=calculatorPostSerializer.data['expression']
                     result=self.__useCalculator(expression)
                     serializer=self.__getSerializedResult(result)
                     return JsonResponse(serializer)

              return JsonResponse(calculatorPostSerializer.errors)
