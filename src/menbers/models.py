from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=300)
    age=models.IntegerField()
    address=models.CharField(max_length=300)
    work=models.CharField(max_length=300)

    def get_info(self):
        return self.name+' '+str(self.age)+' '+self.address+' '+self.work
    
    def __str__(self):
        return self.name+' '+str(self.id)
