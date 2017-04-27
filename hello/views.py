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
import classifier
import pickle
import os

from .models import Greeting
features = []
# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html',context_instance=RequestContext(request))
	
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
        prod_names,prod_images,prod_price,prod_asin,prod_features = psr.SearchProduct(product)
        #return HttpResponse(prod_names)
        #sample = ['lol','ertgf','fghytr','ghgfh','asd','asd']
        global features
        features = prod_features
        product_features_list=[]
        for asin in prod_asin:
            for pf,pa in prod_features:
                if(asin == pa):
                    product_features_list.append(pf)
        product_data = zip(prod_names,prod_images,prod_price,prod_asin,product_features_list)

        #return render_to_response('searchresults.html', {'prod_names':prod_names,'prod_images':prod_images})
        return render_to_response('searchresults.html', {'product_data':product_data},context_instance=RequestContext(request))
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
        
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print ip
    return render_to_response('random.html', {'ip',ip},context_instance=RequestContext(request))

def fetch_reviews(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        product_asin = request.POST.get('product_asin')
        #product_features = request.POST.get('product_features')
        global features
        
        for pf,pa in features:
            if(product_asin == pa):
                product_features = pf
        prod_name,prod_reviews,prod_image = psr.FetchReviews(product_asin)
        prod_emotions = classifier.ClassifyReviews(prod_reviews)
        prod_review_emotion = zip(prod_reviews,prod_emotions)
        #return HttpResponse(prod_emotions)
        return render_to_response('productreviews.html',{'prod_name':prod_name,'prod_review_emotion':prod_review_emotion,'prod_image':prod_image,'prod_features':product_features},context_instance=RequestContext(request))
    else:
        form = NameForm()
        return render(request, 'sorry.html', {'form': form})


