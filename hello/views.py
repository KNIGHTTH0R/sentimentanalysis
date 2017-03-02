from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from .search_button import NameForm
import product_specific_review as psr
from lxml import html
import requests


import requests

from .models import Greeting

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
	
def abstract(request):
    return render(request, 'abstract.html')
	
def random(request):
    return render(request,'random.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def search_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        product = request.POST.get('product_name')
        prod_names = psr.SearchProduct(product)
        #return HttpResponse(prod_names)
        sample = ['lol','ertgf','fghytr','ghgfh','asd','asd']
        return render_to_response('random.html', {'prodnames':prod_names})
        #return HttpResponse(newstring)
        # check whether it's valid:
        '''
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("self.cleaned_data")
            return HttpResponseRedirect('/thanks/')
        else:
            return render(request, 'random.html', {'name': form.cleaned_data})
        '''

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

        return render(request, 'random.html', {'form': form})


