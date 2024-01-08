from django.contrib import admin
from .models import Project, Category
<<<<<<< HEAD
=======
from django.contrib.gis.db import models

>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    
<<<<<<< HEAD
    
    

    
=======
  

>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9

