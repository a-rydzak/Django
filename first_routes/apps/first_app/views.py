from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    response = redirect('/first_app/')
    return response

def show(request, number):
    response = "placeholder to display blog " + str(number)
    return HttpResponse(response)


def edit(requet, number):
    response = "placeholder to edit blog " + str(number)
    return HttpResponse(response)

def destroy(request, number):
    response = redirect('/first_app/')
    return response

def create_again(request):

    if request.method == "POST":
        print("*"*50)
        # print(request.POST)
        # print(request.POST['name'])
        # print(request.POST['desc'])
        # print(request.session)
        # request.session['name'] = "test"  # more on session below
        # print(request.session['name'])
        # print("*"*50)
        # {{request.session.name}} in the html
        return redirect("/first_app/")
    else:
        return redirect("/first_app/")

def html(request):

    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }

    return render(request, './first_app/index.html', context)