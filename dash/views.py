from django.shortcuts import render

# Create your views here.

def dashboard(request):
    hello = 'Hello world'
    return render(request, 'dash/index.html', {
        'hello': hello
    })
    
    
def portfolio_admin(request):
    hello = 'Hello world'
    return render(request, 'dash/port-admin.html', {
        'hello': hello
    })