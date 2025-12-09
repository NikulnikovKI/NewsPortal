from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateFilter
from .models import Post, Author
import django_filters
from django import forms


class PostFilter(FilterSet):
    author = ModelChoiceFilter(queryset=Author.objects.all(), label="Автор", empty_label="Все авторы")
    title = CharFilter(label="Заголовок", lookup_expr="iregex")
    text = CharFilter(label="Содержание", lookup_expr="iregex")
    dateCreation__gt = DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Позже даты',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'dateCreation__gt']

