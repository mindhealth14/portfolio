from django.shortcuts import render, HttpResponse,  HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProjectSerializer, CategorySerializer
from myport.models import Project, Category
import requests

from django.contrib.auth import authenticate, login, logout




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dash:dashboard-admin"))
        else:
            return render(request, "dash/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "mail/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("feed:index"))



@api_view(['GET'])
def portOverview(request):
    api_urls = {
        'List': 'port/port-list/',
        'Detail View': 'port/port-detail/<str:pk>/',
        'Create': 'port/port-create/',
        'Update': 'port/port-update/<int:pk>/',
        'Delete': 'port/port-delete/<str:pk>/',
    }

    return Response(api_urls)


@login_required
@api_view(['GET'])
def portList(request):
    posts = Project.objects.all().order_by('-id')
    serializer = ProjectSerializer(posts, many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def portDetail(request, pk):
	posts = Project.objects.get(id=pk)
	serializer = ProjectSerializer(posts, many=False)
	return Response(serializer.data)


@login_required
@api_view(['POST'])
def createPort(request):
    serializer = ProjectSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
@api_view(['POST'])
def updatePort(request, pk):
    try:
        post = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(post, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
@api_view(['DELETE'])
def deletePort(request, pk):
    post = Project.objects.get(id=pk)
    post.delete()
              
    return Response('Post deleted successfully')


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
