from django.urls import path
from . import views
from .views import CategoryListView



urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    
    # api 
    path("view/", views.portOverview, name='api-overview'),
    path("port/port-list/", views.portList, name='list-view'),
    path("port/port-detail/<int:pk>", views.portDetail, name='list-detail'),
    path("port/port-create/", views.createPort, name='create-port'),
    path("port/port-update/<int:pk>/", views.updatePort, name='update-port'),
    path("port/port-delete/<int:pk>/", views.deletePort, name='delete-port'),
    path('port/categories/', CategoryListView.as_view(), name='category-list'),
    
]