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

def sorry(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'sorry.html')

def underdevelopment(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'underdevelopment.html')
	

def searchresults(request):
    return render(request, 'searchresults.html')

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
        prod_names,prod_images,prod_price,prod_asin = psr.SearchProduct(product)
        #return HttpResponse(prod_names)
        #sample = ['lol','ertgf','fghytr','ghgfh','asd','asd']
        product_data = zip(prod_names,prod_images,prod_price,prod_asin)

        #return render_to_response('searchresults.html', {'prod_names':prod_names,'prod_images':prod_images})
        return render_to_response('searchresults.html', {'product_data':product_data})
        #return HttpResponse(newstring)
        # check whether it's valid:
        '''
        if form.is_valid():
            # process the data in form.cleaned_data as required
        else:
            return render(request, 'random.html', {'name': form.cleaned_data})
        '''
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return render(request, 'sorry.html', {'form': form})


