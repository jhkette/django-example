from django.contrib import admin

# Register your models here.
# Register your models here.
# This is where we customise admin content for the Realtor app
# This is so we can add Realtor models to admin.


from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)