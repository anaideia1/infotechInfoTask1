from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name="post_list"),
    path('newest/', views.PostsNewestListView.as_view(), name="post_newest"),
    path('new/', views.PostCreateView.as_view(), name="post_new"),
    path("users_posts/", views.UserPostsView.as_view(), name="users_posts"),
]