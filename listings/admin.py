from django.contrib import admin

# Register your models here.
# This is where we customise admin content for the listings app
# This is so we can add listings models to admin.


from .models import Listing



class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')


admin.site.register(Listing, ListingAdmin)