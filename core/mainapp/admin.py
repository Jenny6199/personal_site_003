from django.contrib import admin
from .models import Author, Article, ArticleCategory


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin-panel indications for table Author"""
    list_display = [
        'surname',
        'name',
        'parent_name',
        'article_counter',
        'speciality',
        'registered_at',
    ]
    prepopulated_fields = {'slug': ('surname', 'name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin-panel indications for table Article"""
    list_display = [
        'title',
        'category',
        'author',
        'image',
        'created_time',
        'updated_time',
        'visitors_counter',
        'is_published'
    ]
    list_filter = [
        'category',
        'author',
        'created_time',
        'visitors_counter',
        'is_published'
    ]
    search_fields = [
        'title',
    ]
    date_hierarchy = 'created_time'
    ordering = [
        'created_time'
    ]


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    """Admin-panel indications for table ArticleCategory"""
    list_display = ['name', 'slug']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
