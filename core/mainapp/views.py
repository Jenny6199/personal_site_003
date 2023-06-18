from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def check_request(request):
    """example of use variable request"""
    if request.GET:
        print(request.GET)
    return


def index(request):
    """
    main page
    :param request
    :return HttpResponse
    """
    check_request(request)
    return HttpResponse("<h1>Главная страница сайта</h1>")


def categories(request, cat_id):
    """
    categories page
    :param request
    :param cat_id
    :return HttpResponse
    """
    check_request(request)
    return HttpResponse(f"<h1>Страница категорий</h1><p>{cat_id}</p>")


def archive(request, year):
    """
    archive page
    :param request
    :param year - time
    :return HttpResponse
    """
    check_request(request)
    if int(year) > 2023:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    """
    Page 404
    :param request
    :param exception
    :return HttpResponse
    """
    check_request(request)
    if exception:
        print(exception)
    return HttpResponseNotFound('<h1>Запрашиваемая страница не найдена</h1>')
