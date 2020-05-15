from django.shortcuts import render
# we need to import these modules for pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Listing

def index(request):
    # orderby list data - adding a minus so earliest is first
    listings = Listing.objects.all().order_by('-list_date')
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
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')