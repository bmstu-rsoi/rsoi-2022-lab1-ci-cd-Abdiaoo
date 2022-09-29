from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .serializers import PersonsSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.template import loader
@api_view(['GET','POST'])
def listPersons(request,format=None):
    if request.method=='GET':
        persons=Person.objects.all()
        serializer=PersonsSerializer(persons,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        serializer=PersonsSerializer(data=request.data)
        if serializer.is_valid():
            obj=serializer.save()
            response=Response(serializer.data,status=status.HTTP_201_CREATED)
            response['Location']=obj.get_absolute_url()
            return response
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def aSpecificPersons(request,id,format=None):
    try:
        person=Person.objects.get(id=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=PersonsSerializer(person)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serializer=PersonsSerializer(person,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
