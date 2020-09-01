from django.views import generic
from django.urls import reverse_lazy

from core.models import Post

from django.utils import timezone
from datetime import timedelta


class PostsListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_ordering(self):
        order = self.request.GET.get('order', 'asc')
        return order

    def get_queryset(self):
        order = self.get_ordering()
        if order == "asc":
            return Post.objects.all().order_by("publish")
        elif order == "desc":
            return Post.objects.all().order_by("-publish")


class PostsNewestListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().filter(publish__gt=timezone.now() - timedelta(days=1))
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'img']
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)


class UserPostsView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__id=user.pk)