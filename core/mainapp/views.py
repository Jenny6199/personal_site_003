from django.shortcuts import render
from .models import Author, Article


def index(request):
    articles = Article.objects.all()
    context = {
        'title': 'главная',
        'menu': None,
        'articles': articles,
    }
    return render(request, 'mainapp/index.html', context=context)


def contacts(request):
    context = {
        'title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', context=context)
