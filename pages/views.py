from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import bedroom_choices, price_choices

from listings.models import Listings
from realtors.models import Realtor


def index(request):
    allListings = Listings.objects.order_by('-list_date').filter(is_published = True)[:3]

    context = {
        'allListings': allListings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    allRealtors = Realtor.objects.order_by('hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)

    context = {
        'allRealtors': allRealtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
