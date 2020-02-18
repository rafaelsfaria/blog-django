from functools import reduce
from .models import Post, Category
from django.db.models import Q
import operator
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'blog_posts'
    ordering = ['-pub_date']
    paginate_by = 3

    def get_queryset(self):
        result = super(HomeView, self).get_queryset()
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


class PostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryDetail(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.filter(
            category__id=context['category'].id)
        return context
