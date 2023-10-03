from django.urls import path
from .views import index, contacts, news, \
    ArticlesPage, AddArticle, AddAuthor, ArticleRead, ArticlesByCategories

urlpatterns = [
    # Mainpage
    path(route="", view=index, name='index', kwargs={}),
    # Articles
    path(route="articles/", view=ArticlesPage.as_view(), name='articles', kwargs={}),
    path(route="articles/categories/<slug:cat_slug>/", view=ArticlesByCategories.as_view(), name='articles_categories',
         kwargs={'slug': 'cat_slug'}),
    path(route="article/<slug:article_slug>/", view=ArticleRead.as_view(), name='show_article',
         kwargs={'slug': 'article_slug'}),
    path(route="add_article/", view=AddArticle.as_view(), name='add_article', kwargs={}),
    # Authors
    path(route="add_author/", view=AddAuthor.as_view(), name='add_author', kwargs={}),
    # News
    path(route="news/", view=news, name='news', kwargs={}),
    # Contacts
    path(route="contacts/", view=contacts, name='contacts', kwargs={}),
]
