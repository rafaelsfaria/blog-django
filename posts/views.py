from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'posts/index.html'
	context_object_name = 'blog_posts'
	ordering = ['-pub_date']
	paginate_by = 3

class PostView(LoginRequiredMixin, DetailView):
	model = Post
	template_name = 'posts/detail.html'
	context_object_name = 'post'

class PostCreate(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'posts/create.html'
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class CategoryDetail(LoginRequiredMixin, DetailView):
	model = Category
	template_name = 'categories/detail.html'
	context_object_name = 'category'