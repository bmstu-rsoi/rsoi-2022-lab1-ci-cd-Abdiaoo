from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=300)
    age=models.IntegerField()
    adresse=models.CharField(max_length=300)
    work=models.CharField(max_length=300)

    def get_info(self):
        return self.name+' '+str(self.age)+' '+self.adresse+' '+self.work
    
    def __str__(self):
        return self.name+' '+str(self.id)
