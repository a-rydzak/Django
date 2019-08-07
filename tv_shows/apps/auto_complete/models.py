# Inside models.py
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class PersonManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['first_name']) < 1:
            errors['title'] = 'Show name cannot be empty.'

        if len(postData['last_name']) < 5:
            errors['desc'] = 'Show description should be at least 5 characters.'


        return errors
class User(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    objects = PersonManager()
    updated_at = models.DateTimeField(auto_now = True)
