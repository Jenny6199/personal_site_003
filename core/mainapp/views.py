from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleCategory, Author
from django.views.generic import ListView, DetailView, CreateView


main_menu = {
                'главная': '/',
                'статьи': '/articles',
                'новости': '/news',
                'контакты': '/contacts',
                'ещё': '/',
    }


class ArticlesPage(ListView):
    """
    CBV for Articles page
    Отображение всех статей
    """
    model = Article
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self):
        return Article.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = 'Статьи'
        context['category_list'] = ArticleCategory.objects.all()
        return context


class ArticlesByCategories(ListView):
    """
    CBV for page articles by categories
    """
    model = Article
    context_object_name = 'articles'
    paginate_by = 5
    selected_category = None

    def get_queryset(self):
        self.selected_category = ArticleCategory.objects.get(slug=self.kwargs['cat_slug'])
        return Article.objects.filter(category=self.selected_category.pk, is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = main_menu
        context['title'] = f'Статьи по категориям - {self.selected_category}'
        context['category_list'] = ArticleCategory.objects.all()
        return context


class AddArticle(CreateView):
    """
    CBV for create new article
    Добавление статьи на сайте вне админ панели.
    """
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
    """
    CBV for create new author
    Добавление автора на сайте вне админ панели
    """
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
        context['title'] = f'просмотр статьи - {self.object.title}'
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
