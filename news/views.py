from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from .forms import ArticleForm


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


def article_create(request):
    user = request.user
    if user.is_authenticated:
        form = ArticleForm()
        if request.method == 'POST':
            form = ArticleForm(data=request.POST)
            if form.is_valid:
                article = form.save(commit=False)
                article.author = user
                form.save(commit=True)
                return redirect('index')
            else:
                return render(request, 'news/create.html', {'form': form})
        else:
            return render(request, 'news/create.html', {'form': form})
    else:
        return HttpResponse('You need Authenticate from this web-site for create Article!')


def article_update(request, pk):
    user = request.user
    article = Article.objects.get(id=pk)
    if user == article.author:
        form = ArticleForm(instance=article)
        if request.method == 'POST':
            form = ArticleForm(instance=article, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("OK")
            else:
                return render(request, 'news/update.html', {'form': form, 'article': article})
        else:
            return render(request, 'news/update.html', {'form': form, 'article': article})
    else:
        return HttpResponse('OK')
