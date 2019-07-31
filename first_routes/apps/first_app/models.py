# Inside models.py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    # auto_now takes precedence (obviously, because it updates field each time, 
    # while auto_now_add updates on creation only).
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name, self.desc)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Notice the association made with ForeignKey for a one-to-many relationship
    # There can be many comments to one blog
    blog = models.ForeignKey(Blog, related_name = "comments", on_delete=models.PROTECT)
class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name = "admins")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

'''

from apps.first_app.models import *
pip install ipython
https://tutorial.djangogirls.org/en/django_orm/

Blog.objects.create(name="Bens Fashion", desc="A blog about all my cloths")
    b = Blog(name="Disney Blog", desc="Disney stuff")
    b.name = "Disney Blog!"
    b.desc = "Disney stuff!!!"
    b.save()

Blog.objects.first() - retrieves the first record in the Blog table
Blog.objects.last() - retrieves the last record in the Blog table
Blog.objects.all() - retrieves all records in the Blog table
Blog.objects.count() 

Blog.objects.first().__dict__ 
Blog.objects.all().values() 


b = Blog.objects.first() # gets the first record in the blogs table
b.name = "CodingDojo Blog"  # set name to be "CodingDojo Blog"
b.save() # updates the blog record

b = Blog.objects.get(id=1)
b.delete() # deletes that particular record

Blog.objects.get(id=1) - retrieves where id is 1; get() retrieves one and only one record. It will return an error if it finds fewer than or more than one match.
Blog.objects.filter(name="mike") - retrieves records where name is "mike"; returns multiple records
Blog.objects.exclude(name="mike") - opposite of filter; returns multiple records
Blog.objects.order_by("created_at") - orders by created_date field
Blog.objects.order_by("-created_at") - reverses the order
Blog.objects.raw("SELECT * FROM {{app_name}}_{{class/table name}}") - performs a raw SQL query
Blog.objects.first().comments.all() - grabs all comments from the first Blog
Blog.objects.get(id=15).comments.first() - grabs the first comment from Blog id = 15
Comment.objects.get(id=15).blog.name - returns the name of the blog where Comment id = 15 belongs to

Comment.objects.create(blog=Blog.objects.get(id=1), comment="test") - create a new comment where the comment's blog points to Blog.objects.get(id=1).

Admin.objects.filter(first_name__startswith="S") - filters objects with first_name that starts with "S"
Admin.objects.exclude(first_name__contains="E") - excludes objects where first_name contains "E"
Admin.objects.filter(age__gt=80)  - filters objects with age greater than 80


admin = Admin.objects.filter(last_name__contains="o").exclude(first_name__contains="o")
admin = Admin.objects.filter(age__lt=70).filter(first_name__startswith="S")
admin = Admin.objects.filter(age__lt=70, first_name__startswith="S")
admin = Admin.objects.filter(age__lt=70)|Admin.objects.filter(first_name__startswith="S")


class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name, self.desc)
'''

'''
When to use DJANGO
You need to develop a web app or API backend.

You need to move fast, deploy fast, and also make changes as you move ahead.

The app must be secure from most common vulnerabilities and attacks by default. 
For example CSRF, SQL Injection, XSS, Clickjacking, etc.

Your app might scale up/down at any point of time.

You might integrate cutting edge tech in future, eg. Machine Learning.

You need to use a reliable framework which is actively developed, 
and used by many top websites and companies on the planet.

You need both web app and API backend in same codebase to comply
 with “Single source of truth” (aka DRY)

You don’t want to work with database queries directly, and need ORM support.

You want to use open source software.

You’re concerned about finding solutions if you get stuck, so a good documentation and supportive community should be present
'''