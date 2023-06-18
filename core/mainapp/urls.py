from django.urls import path, re_path

from .views import index, categories, archive

urlpatterns = [
    path('', index),
    path('categories/<slug:cat_id>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
