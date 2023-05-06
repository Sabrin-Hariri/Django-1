from django.shortcuts import render
from . import views 
from django.views.generic import *
from . import models
from .models import *
from django.urls import reverse_lazy
# from .forms import CURDForm
from django.urls import reverse
from blog.models import Blog

#################################################################################

def index(request):

     context={'posts':Blog.objects.all(),
               'last_five_post':Blog.objects.all().order_by('-id')[:5],  
               'last_four_post':Blog.objects.all().order_by('-id')[:4]  }
     
     return render(request, 'index.html', context=context)

class ContactPage(TemplateView):
     template_name = "contact.html"


class AboutPage(TemplateView):
     template_name = "about.html"


def show(request,pk):
     context ={}
     context['post']=Blog.objects.get(pk=pk)
     return render(request, 'show.html', context=context)
