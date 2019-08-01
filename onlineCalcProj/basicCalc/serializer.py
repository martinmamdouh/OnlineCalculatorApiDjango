from rest_framework import serializers

class CalculatorResponseSerializer(serializers.Serializer):
    result = serializers.ListField(child=serializers.CharField(),allow_null =True)
    
    error=serializers.CharField(allow_null =True)

class CalculatorPostSerializer(serializers.Serializer):

    expression = serializers.ListField(child=serializers.CharField(),allow_null =True)