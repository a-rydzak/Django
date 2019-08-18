# Inside models.py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Notice the association made with ForeignKey for a one-to-many relationship
    # There can be many comments to one blog
    blog = models.ForeignKey(Blog, related_name = "comments")
class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name = "admins")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
# how dare you
# HELLO MY NAME IS BEN
# DONT TALK TO ME LIKE THAT
'''
Column types
You can find a full list of allowed column types in the documentation, but here are some of the main 
ones you'll be using.

CharField
Any text that a user may enter. This has one additional required parameter, 
max_length, that (unsurprisingly) is the maximum length of text that can be saved.

TextField
Like a CharField, but with no maximum length. Your user could copy the entire text of the Harry Potter 
series into the field, and it would save in the database correctly.

IntegerField, BooleanField
Holds integers or booleans, respectively

DateTimeField
Used for date and times, such as timestamps or when a flight 
is scheduled to depart. This field can take two very useful optional parameters, 
auto_now_add=True, which adds the current date/time when object is created, and 
auto_now=True, which automatically updates any time the object is modified.

ForeignKey, ManyToManyField, OneToOneField
Used to indicate a relationship between models (anything that would require a JOIN statement in SQL). 
ForeignKey is for one-to-many relationships and goes in the model on the "many" side, just 
as the foreign key column goes in the SQL table on the "many" side.
'''


# ONE To MANY
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

this_author = Author.objects.get(id=2)
my_book = Book.objects.create(title="Little Women", author=this_author)
# or on one line...
my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

this_author = Author.objects.get(id=2)
books = Book.objects.filter(author=this_author)
# one-line version:
books = Book.objects.filter(author=Author.objects.get(id=2))

books = Book.objects.filter(author__name="Louise May Alcott")
books = Book.objects.filter(author__name__startswith="Lou")

def index(request):
    context = {"authors": Author.objects.all()}
    return render(request, "books/index.html", context)

<h1>Author List</h1>
<copyul>
  {% for author in authors %}
    <li>{{author.name}}
      <ul>
        {% for book in author.books.all %}
          <li><em>{{book.title}}</em></li>
        {% endfor %}
      </ul>
    </li>
  {% endfor %}
</ul>




#Many to Many
class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Publisher(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

'''
As you can see, each publisher can publish many books, and each book can be 
published by many publishers. Unlike with a ForeignKey, it doesn't 
matter which model has the ManyToManyField. 
'''

this_book = Book.objects.get(id=4)
this_publisher = Publisher.objects.get(id=2)
this_publisher.books.add(this_book)

'''
The syntax to see all books from a given publisher is the same as when doing a reverse 
look-up on a ForeignKey relationship: this_publisher.books.all() in your views.py, or 
this_publisher.books.all in a template.

ManyToManyFields are automatically symmetrical. That is, by adding a book to a publisher, 
Django will also automatically add the publisher to the book. This means that we can add 
or look up from the other end without issue, assuming we've specified a related name so 
that Django knows how to refer to the field in the other model. this_book.publishers.add(this_publisher) 
is the same as this_publisher.books.add(this_book), and this_book.publishers.all() will return 
all publishers of a given book.
'''


#---------------------It's Shell Time!  
'''
>>> python manage.py shell
>>> from apps.{{app_name}}.models import *

Creating a new record
    Blog.objects.create({{field1}}="{{value}}", {{field2}}="{{value}}", etc) # creates a new record in the Blog table
        Blog.objects.create(name="Star Wars Blog", desc="Everything about Star Wars") # creates a new blog record
        Blog.objects.create(name="CodingDojo Blog") # creates a new blog record with the empty desc field
    Alternative way of creating a record
        b = Blog(name="Disney Blog", desc="Disney stuff")
        b.name = "Disney Blog!"
        b.desc = "Disney stuff!!!"
        b.save()
    Basic Retrieval
        Blog.objects.first() - retrieves the first record in the Blog table
        Blog.objects.last() - retrieves the last record in the Blog table
        Blog.objects.all() - retrieves all records in the Blog table
        Blog.objects.count() - shows how many records are in the Blog table
    Displaying records
        Blog.objects.first().__dict__ - shows all the values of a single record/object as a dictionary
        Blog.objects.all().values() - as shown in the videos, shows all the values of a QuerySet (QuerySet contains multiple records)
    Updating the record - once you obtain an object that has the record you want to modify, use save() to update the record.  For example
        b = Blog.objects.first() # gets the first record in the blogs table
        b.name = "CodingDojo Blog"  # set name to be "CodingDojo Blog"
        b.save() # updates the blog record
    Deleting the record - use delete().  For example
        created_at = models.DateTimeField(default=timezone.now)
        author = models.ForeignKey(User,on_delete=models.CASCADE )
        b = Blog.objects.get(id=1)
        b.delete() # deletes that particular record
    Other methods to retrieve records
        Blog.objects.get(id=1) - retrieves where id is 1; get() retrieves one and only one record. It will return an error if it finds fewer than or more than one match.
        Blog.objects.filter(name="mike") - retrieves records where name is "mike"; returns multiple records
        Blog.objects.exclude(name="mike") - opposite of filter; returns multiple records
        Blog.objects.order_by("created_at") - orders by created_date field
        Blog.objects.order_by("-created_at") - reverses the order
        Blog.objects.raw("SELECT * FROM {{app_name}}_{{class/table name}}") - performs a raw SQL query
        Blog.objects.first().comments.all() - grabs all comments from the first Blog
        Blog.objects.get(id=15).comments.first() - grabs the first comment from Blog id = 15
        Comment.objects.get(id=15).blog.name - returns the name of the blog where Comment id = 15 belongs to
    Setting Relationship
        Comment.objects.create(blog=Blog.objects.get(id=1), comment="test") - create a new comment where the comment's blog points to Blog.objects.get(id=1).
'''

# Inside models.py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Notice the association made with ForeignKey for a one-to-many relationship
    # There can be many comments to one blog
    blog = models.ForeignKey(Blog, related_name = "comments")
class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name = "admins")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

'''
Column types
You can find a full list of allowed column types in the documentation, but here are some of the main 
ones you'll be using.

CharField
Any text that a user may enter. This has one additional required parameter, 
max_length, that (unsurprisingly) is the maximum length of text that can be saved.

TextField
Like a CharField, but with no maximum length. Your user could copy the entire text of the Harry Potter 
series into the field, and it would save in the database correctly.

IntegerField, BooleanField
Holds integers or booleans, respectively

DateTimeField
Used for date and times, such as timestamps or when a flight 
is scheduled to depart. This field can take two very useful optional parameters, 
auto_now_add=True, which adds the current date/time when object is created, and 
auto_now=True, which automatically updates any time the object is modified.

ForeignKey, ManyToManyField, OneToOneField
Used to indicate a relationship between models (anything that would require a JOIN statement in SQL). 
ForeignKey is for one-to-many relationships and goes in the model on the "many" side, just 
as the foreign key column goes in the SQL table on the "many" side.
'''


# ONE To MANY
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

this_author = Author.objects.get(id=2)
my_book = Book.objects.create(title="Little Women", author=this_author)
# or on one line...
my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

this_author = Author.objects.get(id=2)
books = Book.objects.filter(author=this_author)
# one-line version:
books = Book.objects.filter(author=Author.objects.get(id=2))

books = Book.objects.filter(author__name="Louise May Alcott")
books = Book.objects.filter(author__name__startswith="Lou")

def index(request):
    context = {"authors": Author.objects.all()}
    return render(request, "books/index.html", context)

<h1>Author List</h1>
<copyul>
  {% for author in authors %}
    <li>{{author.name}}
      <ul>
        {% for book in author.books.all %}
          <li><em>{{book.title}}</em></li>
        {% endfor %}
      </ul>
    </li>
  {% endfor %}
</ul>




#Many to Many
class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Publisher(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

'''
As you can see, each publisher can publish many books, and each book can be 
published by many publishers. Unlike with a ForeignKey, it doesn't 
matter which model has the ManyToManyField. 
'''

this_book = Book.objects.get(id=4)
this_publisher = Publisher.objects.get(id=2)
this_publisher.books.add(this_book)

'''
The syntax to see all books from a given publisher is the same as when doing a reverse 
look-up on a ForeignKey relationship: this_publisher.books.all() in your views.py, or 
this_publisher.books.all in a template.

ManyToManyFields are automatically symmetrical. That is, by adding a book to a publisher, 
Django will also automatically add the publisher to the book. This means that we can add 
or look up from the other end without issue, assuming we've specified a related name so 
that Django knows how to refer to the field in the other model. this_book.publishers.add(this_publisher) 
is the same as this_publisher.books.add(this_book), and this_book.publishers.all() will return 
all publishers of a given book.
'''


#---------------------It's Shell Time!  
'''
>>> python manage.py shell
>>> from apps.{{app_name}}.models import *

Creating a new record
    Blog.objects.create({{field1}}="{{value}}", {{field2}}="{{value}}", etc) # creates a new record in the Blog table
        Blog.objects.create(name="Star Wars Blog", desc="Everything about Star Wars") # creates a new blog record
        Blog.objects.create(name="CodingDojo Blog") # creates a new blog record with the empty desc field
    Alternative way of creating a record
        b = Blog(name="Disney Blog", desc="Disney stuff")
        b.name = "Disney Blog!"
        b.desc = "Disney stuff!!!"
        b.save()
    Basic Retrieval
        Blog.objects.first() - retrieves the first record in the Blog table
        Blog.objects.last() - retrieves the last record in the Blog table
        Blog.objects.all() - retrieves all records in the Blog table
        Blog.objects.count() - shows how many records are in the Blog table
    Displaying records
        Blog.objects.first().__dict__ - shows all the values of a single record/object as a dictionary
        Blog.objects.all().values() - as shown in the videos, shows all the values of a QuerySet (QuerySet contains multiple records)
    Updating the record - once you obtain an object that has the record you want to modify, use save() to update the record.  For example
        b = Blog.objects.first() # gets the first record in the blogs table
        b.name = "CodingDojo Blog"  # set name to be "CodingDojo Blog"
        b.save() # updates the blog record
    Deleting the record - use delete().  For example
        b = Blog.objects.get(id=1)
        b.delete() # deletes that particular record
    Other methods to retrieve records
        Blog.objects.get(id=1) - retrieves where id is 1; get() retrieves one and only one record. It will return an error if it finds fewer than or more than one match.
        Blog.objects.filter(name="mike") - retrieves records where name is "mike"; returns multiple records
        Blog.objects.exclude(name="mike") - opposite of filter; returns multiple records
        Blog.objects.order_by("created_at") - orders by created_date field
        Blog.objects.order_by("-created_at") - reverses the order
        Blog.objects.raw("SELECT * FROM {{app_name}}_{{class/table name}}") - performs a raw SQL query
        Blog.objects.first().comments.all() - grabs all comments from the first Blog
        Blog.objects.get(id=15).comments.first() - grabs the first comment from Blog id = 15
        Comment.objects.get(id=15).blog.name - returns the name of the blog where Comment id = 15 belongs to
    Setting Relationship
        Comment.objects.create(blog=Blog.objects.get(id=1), comment="test") - create a new comment where the comment's blog points to Blog.objects.get(id=1).
'''

# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors


class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()    # add this line!


'''
   Multiple Databases
  https://docs.djangoproject.com/en/2.2/ref/settings/#databases
  https://docs.djangoproject.com/en/2.2/topics/db/multi-db/

Other database settings

DATABASES = {
'default': {},
    'auth_db': {
        'NAME': 'auth_db',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'swordfish',
    },
    'primary': {
        'NAME': 'primary',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'spam',
    },
    'replica1': {
        'NAME': 'replica1',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'eggs',
    },
    'replica2': {
        'NAME': 'replica2',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'bacon',
    },

./manage.py migrate
./manage.py migrate --database=users

$ ./manage.py migrate --database=users
$ ./manage.py migrate --database=customers

}
'''