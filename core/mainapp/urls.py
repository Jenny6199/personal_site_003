from django.urls import path
from .views import index, contacts, articles, news

urlpatterns = [
    path(route="", view=index, name='index', kwargs={}),
    path(route="articles/", view=articles, name='articles', kwargs={}),
    path(route="news/", view=news, name='news', kwargs={}),
    path(route="contacts/", view=contacts, name='contacts', kwargs={}),
]
