from django.urls import path
from . import views

app_name = 'dash'

urlpatterns = [
   path('dashboard-admin/', views.dashboard, name='dashboard-admin'),
   path('dashboard-admin-portfolio/', views.portfolio_admin, name='dashboard-admin-portfolio')
]