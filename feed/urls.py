from django.urls import path
from . import views


app_name = 'feed'


urlpatterns = [
     path("", views.homepage, name='index'),
     path("post_detail/<int:id>/<slug:slug>/", views.post_detail, name='post_detail'),
  
    
]