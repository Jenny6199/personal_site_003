from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Article
from .forms import AddArticleForm

main_menu = {
                'главная': '/',
                'статьи': '/articles',
                'новости': '/news',
                'контакты': '/contacts',
                'ещё': '/',
    }


def index(request):
    """view for mainpage"""
    with open(
            'mainapp/templates/mainapp/text/mainpage_info.txt',
            'r',
            encoding='UTF-8',
    ) as file:
        info = file.read()

    context = {
        'title': 'главная',
        'info': info,
        'menu': main_menu,
    }
    return render(request, 'mainapp/index.html', context=context)


def articles(request):
    """view for page articles"""
    articles_list = Article.objects.all()
    context = {
        'title': 'статьи',
        'articles': articles_list,
        'menu': main_menu,
    }
    return render(request, 'mainapp/articles.html', context=context)


def add_article(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articles'))
    else:
        form = AddArticleForm()
    context = {
        'title': 'добавление статьи',
        'menu': main_menu,
        'form': form,
    }
    return render(request, 'mainapp/add_article.html', context=context)


def news(request):
    """view for page news"""
    context = {
        'title': 'новости',
        'menu': main_menu,
    }
    return render(request, 'mainapp/news.html', context=context)


def contacts(request):
    """view for page contacts"""
    with open(
            'mainapp/templates/mainapp/text/contactspage_info.txt',
            'r',
            encoding='UTF-8',
    ) as file:
        info = file.read()
    context = {
        'title': 'контакты',
        'info': info,
        'menu': main_menu,
    }
    return render(request, 'mainapp/contacts.html', context=context)


def show_article(request, article_id):
    """view for read_article page"""
    article = Article.objects.filter(pk=article_id)[0]
    context = {
        'title': 'просмотр статьи',
        'text': article.text,
        'menu': main_menu,
    }
    return render(request, 'mainapp/read_article.html', context=context)
