from django.shortcuts import render
from .models import Post, Category
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView, 
	UpdateView,
	DeleteView,
)



# Create your views here.


class PostList(ListView):
	model = Post

class PostDetail(DetailView):
	model = Post

class PostCreation(CreateView):
	model = Post
	success_url = reverse_lazy('Post:list')
	fields = ['tittle', 'text', 'category', 'image',]

class PostUpdate(UpdateView):
	model = Post
	success_url = reverse_lazy('Post:list')
	fields = ['tittle', 'text', 'category', 'image',]


class PostDelete(DeleteView):
	model = Post
	success_url = reverse_lazy('courses:list',)