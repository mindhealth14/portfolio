from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from .forms import CreatePostForm

# Create your views here.



def homepage(request):
    names = User.objects.all()
    posts = Post.objects.all()
     
    
    return render(request, 'feed/home.html', {
        'posts': posts,
        'names': names,
      
    })


def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    return render(request, 'feed/detail.html', {
        'post': post
    })
    
