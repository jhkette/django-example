from django.contrib import admin

# Register your models here.
# Register your models here.
# This is where we customise admin content for the Realtor app
# This is so we can add Realtor models to admin.


from .models import Realtor

admin.site.register(Realtor)