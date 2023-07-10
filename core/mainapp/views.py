from django.shortcuts import render
from .models import Article


def index(request):
    """view for mainpage"""
    with open(
            'mainapp/templates/mainapp/mainpage_info.txt',
            'r',
            encoding='UTF-8',
    ) as file:
        info = file.read()

    context = {
        'title': 'главная',
        'info': info,
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


def news(request):
    """view for page news"""
    context = {
        'title': 'новости',
    }
    return render(request, 'mainapp/news.html', context=context)


def contacts(request):
    """view for page contacts"""
    context = {
        'title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', context=context)
