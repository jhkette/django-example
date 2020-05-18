from django.shortcuts import render, get_object_or_404
# we need to import these modules for pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Listing

# here we are importing everything from the choices file in the listings folder
# (this is imported as listings.choices). We are importing the objects
from .choices import price_choices, bedroom_choices, state_choices

def index(request):
    # orderby list data - adding a minus so earliest is first
    # also filter for is_published = true
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)
    # For pagingation please see django docs
    # https://docs.djangoproject.com/en/3.0/topics/pagination/
    paginator = Paginator(listings, 3)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    
    return render(request, 'listings/listings.html', context)


#  we are adding the listing_id, this is in the urls as a parameter 
# so we need to pass it in here
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    # These are a set of queries for the search field
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # see field lookups in django docs for good explanation
            # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#field-lookups
            # we are using __icontains here to search a large body of text
            queryset_list = queryset_list.filter(description__icontains=keywords)
     # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # exact city
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state: 
            # exact match
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # lte = less than or equal to
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            # lte = less than or equal to
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
       
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        # nb here we are adding the dictionary from the posted
        # form so we can represent the data to the user.
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)