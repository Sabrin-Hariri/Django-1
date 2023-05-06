from django import forms
from .models import Blog


class CRUDform(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control" , "placeholder" : "title" }))
    blog_type = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control" , "placeholder" : "type" }))
    description = forms.CharField( widget=forms.Textarea(attrs={
        "class":"form-control" , "placeholder" : "description" }))
    image = forms.ImageField()
    
    class Meta : 
        model=Blog
        fields=['title' , 'blog_type','description' ,'image']


