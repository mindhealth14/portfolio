from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category, Project
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import EmailContactForm

# Create your views here.



    
def about(request):
    name = 'Peter Omoruyi'
    return render(request, 'myport/portfolio/about.html', {
        'name': name,
    })
    
def contact(request):
    
    sent = False
    if request.method == 'POST':
        # submit the form 
        form = EmailContactForm(request.POST)
        if form.is_valid():
            # form pass validation
            cd = form.cleaned_data
            subject = f"{cd['subject']} " 
            sender_email = f"{cd['email']} " 
            message = f"{cd['full_name']} \'s comments: {cd['comments']}"
            send_mail(subject, message, 'mindhealth14@hotmail.com', ['mindhealth14@gmail.com', sender_email] )
            sent = True
            
    else:
        form = EmailContactForm()
        
    return render(request, 'myport/portfolio/contact.html', {
        'form': form,
        'sent': sent
    })
    
    
    
    
    
    
    return render(request, 'myport/project/contact.html', {
        'hello': hello, 
    })
    
def tutorial(request):
    message = 'We are coming soon'
    return render(request, 'myport/portfolio/tutorial.html', {
        'message': message, 
    })

def portfolio_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    projects = Project.objects.all()
   
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects  = projects.filter(category=category)
        
    return render(request, 'myport/portfolio/portfolio.html', {
        'category': category,
        'categories': categories,
        'projects': projects,
        
    })
    
    
def portfolio_detail(request, id, slug):
    portfolio = get_object_or_404(Project, id=id, slug=slug)
    return render(request, 'myport/portfolio/detail.html', {
        'portfolio': portfolio
    })






    
    
