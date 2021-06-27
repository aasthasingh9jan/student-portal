from datetime import datetime
import django
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=125)
    phone=models.CharField(max_length=12)
    msg=models.TextField()
    rating=models.TextField()
    date=models.DateField(default=django.utils.timezone.now)
     
    def __str__(self):
        return self.name
