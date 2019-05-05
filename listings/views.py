from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listings


def index(request):
    allListings = Listings.objects.order_by('-list_date').filter(is_published = True)

    paginator = Paginator(allListings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'allListings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
