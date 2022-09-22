from django.test import TestCase
from ..models import Person

class PersonTest(TestCase):
    """ Test module for the person model """
    def setUp(self):
        Person.objects.create(name='abdi',age=21,adresse='baumanskaya',work='sre_devops')
        Person.objects.create(name='abdio',age=21,adresse='baumanskaya',work='sre_devops')
        Person.objects.create(name='abdioo',age=21,adresse='baumanskaya',work='sre_devops')
    
    def test_persons(self):
        abdi=Person.objects.get(id=1)
        dadinos=Person.objects.get(id=2)
        self.assertEqual(abdi.get_info(),"abdi 21 baumanskaya sre_devops")
        self.assertEqual(dadinos.get_info(),"abdio 21 baumanskaya sre_devops")
