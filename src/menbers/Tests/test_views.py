import json
from rest_framework import status
from django.test import TestCase,Client
from django.urls import reverse
from ..models import Person
from ..serializers import PersonsSerializer
client=Client()

class getAllPersons(TestCase):
    """ Test module for GET all Persons API """
    def setUp(self):
        Person.objects.create(name='abdi',age=21,adresse="baumanskaya",work="sre_devops")
        Person.objects.create(name='dadinos',age=21,adresse="baumanskaya",work="sre_devops")
        Person.objects.create(name='dadinos',age=21,adresse="baumanskaya",work="sre_devops")
    def test_all_persons(self):
        response=client.get(reverse('listPersons'))
        persons=Person.objects.all()
        serializer=PersonsSerializer(persons,many=True)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class GetSpecificPerson(TestCase):
    def setUp(self):
        self.person1=Person.objects.create(name='abdi',age=21,adresse='baumanskaya',work='sre_devops')
        self.person2=Person.objects.create(name='martel',age=21,adresse='baumanskaya',work='sre_devops')
        self.person3=Person.objects.create(name='dadinos',age=21,adresse='baumanskaya',work='sre_devops')
        self.person4=Person.objects.create(name='dyna',age=21,adresse='baumanskaya',work='sre_devops')
    
    def test_get_valid_specific_person(self):
        response=client.get(reverse('specificPerson',kwargs={'id':self.person2.id}))
        person=Person.objects.get(id=self.person2.id)
        serializer=PersonsSerializer(person)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_invalid_person(self):
        response=client.get(reverse('specificPerson',kwargs={'id':30}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

class CreateNewPersonTest(TestCase):
    def setUp(self):
        self.valid_person={
            'name':'dadinos',
            'age':21,
            'adresse':'baumanskaya',
            'work':'sre_devops'
        }
        self.invalid_person={
            'name':'',
            'age':21,
            'adresse':'',
            'work':'sre_devops'
        }
    def test_create_valid_person(self):
        response=client.post(
            reverse('listPersons'),
            data=json.dumps(self.valid_person),
            content_type='application/json'
        )
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_create_invalid_person(self):
        response=client.post(
            reverse('listPersons'),
            data=json.dumps(self.invalid_person),
            content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

class UpdateSpecificPersonTest(TestCase):
    def setUp(self):
        self.person1=Person.objects.create(name='abdi',age=21,adresse='baumanskaya',work='sre_devops')
        self.person2=Person.objects.create(name='martel',age=21,adresse='baumanskaya',work='sre_devops')
        self.person3=Person.objects.create(name='dadinos',age=21,adresse='baumanskaya',work='sre_devops')
        self.person4=Person.objects.create(name='dyna',age=21,adresse='baumanskaya',work='sre_devops')
        self.valid_person={
            'name':'dadinos',
            'age':21,
            'adresse':'baumanskaya',
            'work':'sre_devops'
        }
        self.invalid_person={
            'name':'',
            'age':21,
            'adresse':'baumanskaya',
            'work':''
        }

    def test_update_valid_person(self):
        response=client.put(
            reverse('specificPerson',kwargs={'id':self.person2.id}),
            data=json.dumps(self.valid_person),
            content_type='application/json'
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_update_invalid_person(self):
        response=client.put(
            reverse('specificPerson',kwargs={'id':self.person2.id}),
            data=json.dumps(self.invalid_person),
            content_type='application/json'
        )
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

class DeleteSpecificPersonTest(TestCase):
    def setUp(self):
        self.person1=Person.objects.create(name='abdi',age=21,adresse='baumanskaya',work='sre_devops')
        self.person2=Person.objects.create(name='martel',age=21,adresse='baumanskaya',work='sre_devops')
        self.person3=Person.objects.create(name='dadinos',age=21,adresse='baumanskaya',work='sre_devops')
        self.person4=Person.objects.create(name='dyna',age=21,adresse='baumanskaya',work='sre_devops')

    def test_valid_delete_person(self):
        response=client.delete(
            reverse('specificPerson',kwargs={'id':self.person2.id}))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
    
    def test_invalid_delete_person(self):
        response=client.delete(
            reverse('specificPerson',kwargs={'id':30}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
