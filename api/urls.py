from django.urls import path
from . import views



urlpatterns = [
    path("view/", views.postOverview, name='api-overview'),
    path("post/post-list/", views.postList, name='list-view'),
    path("post/post-detail/<int:pk>", views.postDetail, name='list-detail'),
    path("post/post-create/", views.createPost, name='create-post'),
    path("post/post-update/<int:pk>/", views.updatePost, name='update-post'),
    path("post/post-delete/<int:pk>/", views.deletePost, name='delete-post'),
    
]