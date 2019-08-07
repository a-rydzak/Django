from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Count, F, Value # https://docs.djangoproject.com/en/2.2/ref/models/expressions/
from django.db.models.functions import Length, Upper
from .models import *
from datetime import datetime
# the index function is called when root is visited
def index(request):

    context={}
    #title , network ,release_date ,desc
    #Show.objects.create(title = "My SHow", network="55", desc='55', release_date= datetime.strptime('Jun 1 2005 1:33PM', '%b %d %Y %I:%M%p'))
    
    context['shows'] = Show.objects.all()
    
    return render(request, './semi_restful/index.html', context)

def new(request):
    
    if 'create_errors' in request.session:

        messages = {'messages':request.session['create_errors']}
        return render(request, './semi_restful/new.html', messages)

    else:

        return render(request, './semi_restful/new.html')

def create(request):

    if request.method == 'POST':

        request.session['create_errors'] = {}
        errors = Show.objects.basic_validator(request.POST)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                request.session['create_errors'][key] = value
            # redirect the user back to the form to fix the errors
            return redirect('/shows/new')

        else:
            if 'create_errors' in request.session:
                del request.session['create_errors']
            Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=datetime.strptime(request.POST['release_date'], '%Y-%m-%d'), desc=request.POST['desc'])
            return redirect('/shows')

    else:

        if 'create_errors' in request.session:
            del request.session['create_errors']
        return redirect('/shows')


def show(request, show_id):

    show = Show.objects.get(id = show_id)

    context = {
        'id':show.id,
        'title': show.title,
        'network': show.network,
        'release_date': show.release_date,
        'desc': show.desc,
        'last_updated': show.updated_at
    }
    
    return render(request, './semi_restful/show.html', context)

def edit(request, show_id):

    show = Show.objects.get(id = show_id)

    context = {

        'id':show.id,
        'title': show.title,
        'network': show.network,
        'release_date': show.release_date.strftime('%Y-%m-%d'),
        'desc': show.desc,
        'last_updated': show.updated_at
    }
    

    if 'create_errors' in request.session:

        messages = {'messages':request.session['create_errors'],
                    'id':show.id,
                    'title': show.title,
                    'network': show.network,
                    'release_date': show.release_date.strftime('%Y-%m-%d'),
                    'desc': show.desc           
        }

        return render(request, './semi_restful/edit.html', messages)

    else:

        return render(request, './semi_restful/edit.html', context)

def update(request, show_id):

    if request.method == 'POST':

        request.session['create_errors'] = {}
        errors = Show.objects.basic_validator(request.POST)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                request.session['create_errors'][key] = value
            # redirect the user back to the form to fix the errors
            return redirect('/shows/edit/'+show_id)

        else:
            if 'create_errors' in request.session:
                del request.session['create_errors']

            show = Show.objects.get(id = show_id)

            show.title = request.POST['title']
            show.network = request.POST['network']
            show.release_date = datetime.strptime(request.POST['release_date'], '%Y-%m-%d')
            show.desc = request.POST['desc']
            show.save()
            return redirect('/shows/edit/'+show_id)

    else:

        if 'create_errors' in request.session:
            del request.session['create_errors']
        return redirect('/shows')

def delete(request, show_id):

    Show.objects.get(id = show_id).delete()

    return redirect('/shows')