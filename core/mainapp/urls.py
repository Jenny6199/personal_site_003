from django.urls import path
from .views import index, contacts, articles

urlpatterns = [
    path(route="", view=index, name='index', kwargs={}),
    path(route="articles/", view=articles, name='articles', kwargs={}),
    path(route="contacts/", view=contacts, name='contacts', kwargs={}),
]
