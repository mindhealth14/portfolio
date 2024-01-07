from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer
from myport.models import Project, Category
from feed.models import Post
import requests

@api_view(['GET'])
def postOverview(request):
    api_urls = {
        'List': 'post/post-list/',
        'Detail View': 'post/post-detail/<str:pk>/',
        'Create': 'post/post-create/',
        'Update': 'post/post-update/<int:pk>/',
        'Delete': 'post/post-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def postList(request):
    posts = Post.objects.all().order_by('-id')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postDetail(request, pk):
	posts = Post.objects.get(id=pk)
	serializer = PostSerializer(posts, many=False)
	return Response(serializer.data)



@api_view(['POST'])
def createPost(request):
    serializer = PostSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def updatePost(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
              
    return Response('Post deleted successfully')






    
        
        
    
    
        
    
    
    
    