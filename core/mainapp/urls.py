from django.urls import path
from .views import index, contacts, articles, news, show_article

urlpatterns = [
    path(route="", view=index, name='index', kwargs={}),
    path(route="articles/", view=articles, name='articles', kwargs={}),
    path(route="news/", view=news, name='news', kwargs={}),
    path(route="contacts/", view=contacts, name='contacts', kwargs={}),
    path(route="article/<int:article_id>", view=show_article, name='show_article', kwargs={})
]
