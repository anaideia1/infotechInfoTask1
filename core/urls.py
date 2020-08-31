from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name="post_list"),\
    path('reversed/', views.PostsReversedListView.as_view(), name="post_reversed_list"),
    path('newest', views.PostsNewestListView.as_view(), name="post_newest"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('new/', views.PostCreateView.as_view(), name="post_new"),
]