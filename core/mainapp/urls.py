from django.urls import path
from .views import index, contacts

urlpatterns = [
    path(route="", view=index, name='index', kwargs={}),
    path(route="contacts", view=contacts, name='contacts', kwargs={}),
]
