from django.shortcuts import render
from .models import Author, Article


def index(request):
    articles = Article.objects.all()
    context = {
        'title': 'Главная',
        'menu': None,
        'articles': articles,
    }
    return render(request, 'mainapp/index.html', context=context)
