# Inside models.py
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 1:
            errors['title'] = 'Show name cannot be empty.'

        if len(postData['desc']) < 5:
            errors['desc'] = 'Show description should be at least 5 characters.'

        if len(postData['network']) < 1:
            errors['network'] = 'Show network cannot be empty.'

        date_vaild = False

        try:
            date_vaild = datetime.strptime(postData['release_date'], '%Y-%m-%d') <= datetime.now()

        except Exception as e:
            error = e
            date_vaild = False
        finally:
            
            if not date_vaild or postData['release_date']=='' or postData['release_date']==None:
                errors['release_date'] = 'Release date must have been in the past'

        return errors

class Show(models.Model):
    title = models.CharField(max_length= 100)
    network = models.CharField(max_length= 100)
    release_date = models.DateTimeField(null= False)
    desc = models.TextField()
    objects = ShowManager()
    updated_at = models.DateTimeField(auto_now = True)


