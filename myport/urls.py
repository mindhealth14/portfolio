from django.urls import path 
from . import views


app_name = 'myport'

urlpatterns = [
   
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("tutorial/", views.tutorial, name='tutorial'),
    path("portfolio", views.portfolio_list, name='portfolio'),
    path("<slug:category_slug>/", views.portfolio_list, name='project_list_by_category'),
    path("portfolio/<int:id>/<slug:slug>/", views.portfolio_detail, name='project_detail'),
    path("portfolio", views.portfolio_list, name='portfolio'),
    path("<slug:category_slug>/", views.portfolio_list, name='project_list_by_category'),
    path("portfolio/<int:id>/<slug:slug>/", views.portfolio_detail, name='project_detail'),    
]
