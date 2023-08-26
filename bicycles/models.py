from django.db import models

# Create your models here.
class Bicycle(models.Model):
    type = models.CharField()
    make = models.CharField()
    model_name = models.CharField()
    year = models.IntegerField()
    
    def __str__(self):
        return self.bicycle 