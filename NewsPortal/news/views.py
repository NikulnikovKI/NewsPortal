from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from django_filters.views import FilterView
from .forms import PostForm
from django.urls import reverse_lazy
from .utils import create_or_edit


class PostListView(FilterView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/post_list.html'
    ordering = ['-dateCreation']
    paginate_by = 10
    filterset_class = PostFilter


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        context['time_now'] = datetime.utcnow()
        context['total_news'] = Post.objects.filter(categoryType='NW').count()
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_or_edit(context, self.request.path)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_or_edit(context, self.request.path)


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy("post_list")

class NewsSearchView(FilterView):
    model = Post
    template_name = 'news/news_search.html'
    context_object_name = 'posts'
    filterset_class = PostFilter

