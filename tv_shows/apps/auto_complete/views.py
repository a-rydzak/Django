from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from django.core import serializers
import json

def index(request):
    # User.objects.create(first_name="Bill",last_name="Rydzak")
    # User.objects.create(first_name="Joe",last_name="Rydzak")
    # User.objects.create(first_name="Susie",last_name="Villere")
    # User.objects.create(first_name="Jolie",last_name="Villere")
    # User.objects.create(first_name="Crystal",last_name="Villere")
    # User.objects.create(first_name="Batman",last_name="Villere")
    # User.objects.create(first_name="Cole",last_name="Villere")
    # User.objects.create(first_name="Patil",last_name="Villere")
    return render(request, './auto_complete/index.html')


# query = "SELECT first_name, last_name FROM users WHERE first_name LIKE %(starts_with)s OR last_name LIKE %(starts_with)s"
def users_api(request):

    users = User.objects.filter(first_name__startswith=request.POST['starts_with'])

    return render(request, './auto_complete/index.html', {users:users})

def users_api_json(request):
    users = User.objects.filter(first_name__startswith=request.POST['starts_with'])
    return HttpResponse(serializers.serialize("json", users), content_type='application/json')

def users_api_json_two(request):
    users = User.objects.filter(first_name__startswith=request.POST['starts_with'])
    return JsonResponse({'users': list(users.values())})