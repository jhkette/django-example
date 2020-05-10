from django.contrib import admin

# Register your models here.
# This is where we customise admin content for the listings app
# This is so we can add listings models to admin.


from .models import Listing

admin.site.register(Listing)