from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.


class HomeView(ListView):
	model = Post
	template_name = 'posts/index.html'
	context_object_name = 'blog_posts'

class PostView(DetailView):
	model = Post
	template_name = 'posts/detail.html'
	context_object_name = 'post'