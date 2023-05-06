from django.contrib import admin
from django.urls import path 
# from . import views 
from .views import *

urlpatterns = [
    path('',views.index, name= "index" ),
    path('contact/',ContactPage.as_view() , name= "contact" ),
    path('about/',AboutPage.as_view() , name= "about" ),
    path('show/<int:pk>/',views.show , name= "show" ),

]


