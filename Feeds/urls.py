from django.urls import path
from . import views

urlpatterns = [
    path('',views.feed, name='feeds'),
    path('add-post',views.addPost, name='add-post'),
    path('<uuid:post_id>',views.postDetails, name='postdetail'),
    path('<uuid:post_like/like', views.Likes, name='likes')
]
