from django.db import models
from multiselectfield import MultiSelectField
class ContactDetails(models.Model):
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    mobile=models.IntegerField()
    email_id=models.EmailField()
    courses = models.CharField(max_length=100)
    fee = models.IntegerField()
    location = models.CharField(max_length=150)