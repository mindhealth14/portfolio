"""
URL configuration for myportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myport.urls", namespace='myport')),
    path('', include("feed.urls", namespace='feed')),
    path('api/', include("api.urls")),
    path('portapi/', include("portapi.urls")),
    path('dashboard/', include("dash.urls", namespace='dash')),
<<<<<<< HEAD
=======
    path('tutorials/', include("tutorial.urls", namespace='tutorial')),
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
    path('__debug__/', include("debug_toolbar.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
