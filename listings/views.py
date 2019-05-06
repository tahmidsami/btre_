from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import bedroom_choices, price_choices

from .models import Listings


def index(request):
    allListings = Listings.objects.order_by('-list_date').filter(is_published = True)

    paginator = Paginator(allListings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'allListings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listings, pk = listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    query_list = Listings.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']        
        if keywords:
            query_list = query_list.filter(discription__icontains = keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact = city)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte = price)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__exact = bedrooms)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': query_list,
        'values': request.GET,
    }

    return render(request, 'listings/search.html', context)
