from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listings

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {
        'bands': bands, 
        })


def about_us(request):
    return HttpResponse('<h1>ABOUT US</h1>')

def contact_us(request):
    return HttpResponse('<h1>CONTACT US</h1>')

def listings(request):
    listings = Listings.objects.all()
    return HttpResponse(f"""
        <h1>Welcome to the listing section !</h1>
        <p>Voici quelques annonces :<p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
        </ul>
""")