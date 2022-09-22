from rest_framework import serializers
from .models import Person
class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=['id','name','age','address','work']