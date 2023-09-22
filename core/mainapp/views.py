from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleCategory, Author
from .forms import AddArticleForm
from django.views.generic import ListView, DetailView, CreateView

main_menu = {
                'главная': '/',
                'статьи': '/articles',
                'новости': '/news',
                'контакты': '/contacts',
                'ещё': '/',
    }


class ArticlesPage(ListView):
    """CBV for Articles page"""
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = 'Статьи'
        context['category_list'] = ArticleCategory.objects.all()
        return context


class AddArticle(CreateView):
    """CBV for create new article"""
    model = Article
    fields = ['title', 'slug', 'category', 'author', 'image', 'text', ]
    template_name = 'mainapp/add_article.html'
    success_url = '/articles/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = 'Добавление статьи'
        return context

    def form_valid(self, form):
        form.save()
        author = Author.objects.get(pk=form.data['author'])
        author.update_article_counter()
        return super().form_valid(form)


class AddAuthor(CreateView):
    model = Author
    fields = ['surname', 'name', 'parent_name', 'slug', 'speciality', ]
    success_url = '/articles/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = 'Добавление автора'
        context['category_list'] = ArticleCategory.objects.all()
        return context


class ArticleRead(DetailView):
    """class for page read_article"""
    model = Article
    template_name = 'mainapp/read_article.html'

    def get_object(self):
        article = get_object_or_404(Article, slug=self.kwargs['article_slug'])
        article.visitors_counter += 1
        article.save()
        return article

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = f'просмотр статьи - {self.object.slug}'
        context['text'] = self.object.text
        context['menu'] = main_menu
        context['selected_category'] = self.object.category
        return context


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
    """
    view for page articles
    :param - request
    """
    articles_list = Article.objects.filter(is_published=True)
    articles_category_list = ArticleCategory.objects.all()
    context = {
        'title': 'статьи',
        'articles': articles_list,
        'category_list': articles_category_list,
        'menu': main_menu,
    }
    return render(request, 'mainapp/article_list.html', context=context)


def articles_categories(request, cat_slug):
    """
    View for page articles_by_categories
    :param - request
    :param - cat_slug
    """
    selected_category = ArticleCategory.objects.get(slug=cat_slug)
    articles_list = Article.objects.filter(
        category=selected_category.pk,
        is_published=True
    )
    articles_category_list = ArticleCategory.objects.all()
    context = {
        'title': f'статьи по категориям - {selected_category}',
        'articles': articles_list,
        'category_list': articles_category_list,
        'menu': main_menu,
        'cat_selected': selected_category.pk,
    }
    return render(request, 'mainapp/article_list.html', context=context)


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


def show_article(request, article_slug):
    """
    View for read_article page
    :param request
    :param article_slug
    """
    article = get_object_or_404(Article, slug=article_slug)
    article.visitors_counter += 1
    article.save()
    context = {
        'title': 'просмотр статьи',
        'text': article.text,
        'menu': main_menu,
        'selected_category': article.category,
    }
    return render(request, 'mainapp/read_article.html', context=context)


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
