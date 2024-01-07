from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category, Course


# Create your views here.
    
def course_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    courses = Course.objects.all()
   
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        courses  = Course.objects.filter(category=category)
        
    return render(request, 'tutorial/index.html', {
        'category': category,
        'categories': categories,
        'courses': courses,      
    })
    
    
def course_detail(request, id, slug):
    categories = Category.objects.all()
    course = get_object_or_404(Course, id=id, slug=slug)
    return render(request, 'tutorial/detail.html', {
        'course': course,
        'categories': categories,
    })
    
    