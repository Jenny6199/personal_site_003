from django.urls import path
from .views import index, contacts, articles_categories, news, \
    ArticlesPage, AddArticle, AddAuthor, ArticleRead

urlpatterns = [
    # Mainpage
    path(
        route="",
        view=index,
        name='index',
        kwargs={},
    ),

    # RESERVED
    # path(route="articles/", view=articles, name='articles', kwargs={}),
    # path(route="add_article/", view=add_article, name='add_article', kwargs={}),
    # path(route="article/<slug:article_slug>", view=show_article, name='show_article', kwargs={}),

    # CBV - CREATE BASE VIEWS
    # =============================================

    # ARTICLE
    # Article_CREATE
    path(
        route="add_article/",
        view=AddArticle.as_view(),
        name='add_article',
        kwargs={},
    ),
    # Article_all_READ
    path(
        route="articles/",
        view=ArticlesPage.as_view(),
        name='articles',
        kwargs={},
    ),

    # Article_by_categories_READ
    path(
        route="article/<slug:article_slug>/",
        view=ArticleRead.as_view(),
        name='show_article',
        kwargs={'slug': 'article_slug'},
    ),

    # AUTHOR
    # =============================================
    # Author_CREATE
    path(
        route="add_author/",
        view=AddAuthor.as_view(),
        name='add_author',
        kwargs={},
    ),

    # CATEGORIES
    # =============================================
    # Categories_READ
    path(
        route="articles/categories/<slug:cat_slug>/",
        view=articles_categories,
        name='articles_categories',
        kwargs={},
    ),

    # News
    path(
        route="news/",
        view=news,
        name='news',
        kwargs={},
    ),
    # Contacts
    path(
        route="contacts/",
        view=contacts,
        name='contacts',
        kwargs={},
    ),
]
