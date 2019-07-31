from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# the index function is called when root is visited

def landing(request):

    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1 

    context = {
        "string": get_random_string(length=32),
        "count": str(request.session['count'])
    }
    
    return render(request,'random_word_app/index.html', context)

