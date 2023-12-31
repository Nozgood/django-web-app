from django.shortcuts import render, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail

def band_list(request):
    bands = Band.objects.all()

    return render(
        request, 
        'listings/band_list.html', locals()
    )

def band_detail(request, band_id):
    band = Band.objects.get(pk=band_id)
    return render(
        request, 
        'listings/band_detail.html', 
        {
            'band': band
        },
    )

def about_us(request):
    return render(request, 'listings/about.html')

def contact_us(request):
    form = ContactUsForm(request.POST if request.method == "POST" else None)
    form = ContactUsForm((None, request.POST)[request.method == "POST"])

    if request.method == 'POST':

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('contact')

    return render(
        request, 
        'listings/contact.html',
        {
            'form': form,
        }
    )

def listings(request):
    listings = Listing.objects.all()
    return render(
            request, 
            'listings/listings.html', 
            {
                'listings': listings, 
        })

def home(request):
    return render(request, 'listings/home.html')