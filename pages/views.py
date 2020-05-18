from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from listings.models import Listing
from realtors.models import Realtor

# here we are importing everything from the choices file in the listings folder
# (this is imported as listings.choices). We are importing the objects
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'realtors': realtors
    }

    return render(request, 'pages/about.html', context)
