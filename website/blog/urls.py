from django.urls import path 
from . import  views 
from . views import *

urlpatterns = [
    path('',PostList.as_view() , name= "blog" ),
    path('create/',PostCreate.as_view() , name= "create" ),
    path('detail/<int:pk>/',PostDetail.as_view() , name= "detail" ),
    path('update/<int:pk>/',PostUpdate.as_view() , name= "update" ),
    path('delete/<int:pk>/',PostDelete.as_view() , name= "delete" ),
    path('login/',Login.as_view() , name= "login" ),

]


