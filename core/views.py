from django.views import generic

from core.models import Post

from django.utils import timezone
from datetime import timedelta


class PostsListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostsReversedListView(generic.ListView):
    model = Post
    queryset = Post.objects.all()[::-1]
    template_name = 'post_reversed_list.html'
    context_object_name = 'reversed_posts'


class PostsNewestListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().filter(publish__gt=timezone.now() - timedelta(days=1))
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.edit.CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']