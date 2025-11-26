from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/post_list.html'
    ordering = ['-dateCreation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['total_news'] = Post.objects.filter(categoryType='NW').count()
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_detail.html'
