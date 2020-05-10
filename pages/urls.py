from django.urls import path

from  . import views
urlpatterns = [
    # root path and the name 
    # the name can be used in templates
    path('', views.index , name='index'),  
    path('about', views.about , name='about')  
]