from django.urls import path
from . import views

#localhost:800/file
#localhost:800/file/oder

urlpatterns = [
     
    path('', views.file, name='file'),
  
]