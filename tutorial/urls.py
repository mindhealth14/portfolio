from django.urls import path
from . import views


app_name = 'tutorial'


urlpatterns = [
    path('tutorial/', views.course_list, name='courses'),
    path('tutorial/<slug:category_slug>/', views.course_list, name='course_list_by_category'),
     path("portfolio/<int:id>/<slug:slug>/", views.course_detail, name='course_detail'),
    
]