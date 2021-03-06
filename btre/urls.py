"""btre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #need to import
from django.conf.urls.static import static #need to import

# We list all the urls from apps here
# wee add there path and the urls to include.
# We need to import include from django.urls

urlpatterns = [
    path('', include('pages.urls') ),
    path('listings/', include('listings.urls') ),
    path('accounts/', include('accounts.urls') ),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# THE LAST LINE ENSURES MEDIA FILES APPEAR ON FRONT END.
# WE ALSO NEED TO IMPORT THE FILES MENTIONED (see below)
# from django.conf import settings
# from django.conf.urls.static import static
# This is a really good guide on image uploads in DJANGO
# https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial
# https://docs.djangoproject.com/en/3.0/howto/static-files/
