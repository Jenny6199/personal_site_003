from django.contrib import admin
from .models import Author, Article


@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = [
        'surname',
        'name',
        'parent_name',
        'article_counter',
        'speciality',
        'registered_at',
    ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'author',
        'image',
        'created_time',
        'updated_time',
        'visitors_counter',
    ]
