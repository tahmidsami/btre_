from django.shortcuts import render
from django.http import HttpResponse

from .models import Listings


def index(request):
    allListings = Listings.objects.all()

    context = {
        'allListings': allListings
    }

    return render(request, 'listings/listings.html', context)

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
