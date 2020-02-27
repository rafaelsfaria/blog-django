from functools import reduce
from .models import Post, Category
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import operator
# Create your views here.


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'blog_posts'
    ordering = ['-pub_date']
    paginate_by = 3

    def get_queryset(self):
        result = super(PostListView, self).get_queryset()
        query = self.request.GET.get('q')

        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_, (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_, (Q(content__icontains=q) for q in query_list))
            )
        
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class UserPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'blog_posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-pub_date')

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ['title', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ['title', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.filter(
            category__id=context['category'].id)
        return context
