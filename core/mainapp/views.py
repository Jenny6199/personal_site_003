from django.shortcuts import render
from .models import Article


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context=context)


def articles(request):
    """view for page articles"""
    articles_list = Article.objects.all()
    context = {
        'title': 'статьи',
        'articles': articles_list,
    }
    return render(request, 'mainapp/articles.html', context=context)


def contacts(request):
    context = {
        'title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', context=context)
