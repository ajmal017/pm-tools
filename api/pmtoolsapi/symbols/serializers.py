from rest_framework import serializers
from .models import Symbol

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = ['id', 'ticker', 'short_name', 'long_name', 'source']