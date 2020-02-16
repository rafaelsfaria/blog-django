from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.


class HomeView(ListView):
	model = Post
	template_name = 'posts/index.html'
	context_object_name = 'blog_posts'
	ordering = ['-pub_date']
	paginate_by = 3

class PostView(DetailView):
	model = Post
	template_name = 'posts/detail.html'
	context_object_name = 'post'

class PostCreate(CreateView):
	model = Post
	template_name = 'posts/create.html'
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)