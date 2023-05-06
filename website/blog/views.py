from django.shortcuts import render
from django.views.generic import *
from .forms import CRUDform
from django.urls import reverse_lazy ,reverse
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

class Login(LoginView):
    template_name = "login.html"
    redirect_authenticated_user=False 
    def get_success_url(self):
        return reverse_lazy('blog')
    def form_invalid(self , form):
        return self.render_to_response( self.get_context_data(form = form))
    

class PostList(LoginRequiredMixin,ListView):
    model=Blog
    context_object_name ='post'
    template_name = 'blog.html' 


class PostDetail(LoginRequiredMixin,DetailView):
    model=Blog
    context_object_name ='post'
    template_name = 'detail.html' 


class PostCreate(LoginRequiredMixin,CreateView):
    model=Blog
    form_class=CRUDform
    template_name = 'form.html'
    success_url = reverse_lazy('blog')
    
    def from_vaild(self,form):
        form.instance.user =self.reques.user
        return super(PostCreate , self).form_vaild(form)



class PostUpdate(LoginRequiredMixin,UpdateView):
    model=Blog
    form_class=CRUDform
    template_name = 'form.html'
    success_url = reverse_lazy('blog')
    
    def from_vaild(self,form):
        return super(PostUpdate,self).form_vaild(form)


class PostDelete(LoginRequiredMixin,DeleteView):
    model=Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('blog')
    def get_success_url(self):
        return reverse('blog')



    

