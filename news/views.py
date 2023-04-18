from django.shortcuts import render
from .models import Article


# Create your views here.


def index(request):
    return render(request, 'news/index.html')


def home(request):
    articles = Article.objects.filter(is_activate=True)
    return render(request, 'news/home.html', {'articles': articles})


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    articles = Article.objects.filter(is_activate=True)
    return render(request, 'news/detail.html', context={'article': article, 'articles': articles})
