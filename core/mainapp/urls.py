from django.urls import path
from .views import index, contacts, articles, articles_categories, news, show_article, add_article, \
    ArticlesPage

urlpatterns = [
    # Mainpage
    path(route="", view=index, name='index', kwargs={}),
    # Articles page
    # path(route="articles/", view=articles, name='articles', kwargs={}),
    # CBV
    path(route="articles/", view=ArticlesPage.as_view(), name='articles', kwargs={}),
    path(route="articles/categories/<slug:cat_slug>/", view=articles_categories, name='articles_categories', kwargs={}),
    path(route="article/<slug:article_slug>", view=show_article, name='show_article', kwargs={}),
    path(route="add_article/", view=add_article, name='add_article', kwargs={}),
    # News
    path(route="news/", view=news, name='news', kwargs={}),
    # Contacts
    path(route="contacts/", view=contacts, name='contacts', kwargs={}),
]
