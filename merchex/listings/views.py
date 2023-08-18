from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listings

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {
        'bands': bands, 
        })


def about_us(request):
    return render(request, 'listings/about.html')

def contact_us(request):
    return render(request, 'listings/contact.html')

def listings(request):
    listings = Listings.objects.all()
    return render(
            request, 
            'listings/listings.html', 
            {
                'listings': listings, 
        })