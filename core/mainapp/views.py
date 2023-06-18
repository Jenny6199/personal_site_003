from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Главная страница сайта</h1>")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Страница категорий</h1><p>{cat_id}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
