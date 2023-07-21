from django.db import models
from django.urls import reverse


class Author(models.Model):
    """
    Model for author for site's mainapp
    """
    # Fields
    surname = models.CharField(max_length=62, verbose_name='фамилия')
    name = models.CharField(max_length=62, verbose_name='имя')
    parent_name = models.CharField(max_length=62, verbose_name='отчество', blank=True)
    article_counter = models.PositiveIntegerField(default=0, verbose_name='количество статей')
    speciality = models.CharField(max_length=128, verbose_name='специальность')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')

    # Metadata
    class Meta:
        ordering = ['surname']
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    # Methods
    def __str__(self):
        return f'{self.surname} {self.name}'


class Article(models.Model):
    """
    Model for article for site's mainapp
    """
    # Fields
    title = models.CharField(max_length=255, verbose_name='заголовок', blank=False)
    category = models.CharField(max_length=128, blank=False, verbose_name='категория')
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               verbose_name='автор',
                               unique=False,
                               db_constraint=False,
                               blank=False,
                               )
    image = models.ImageField(blank=True, upload_to='images/', verbose_name='изображение')
    text = models.TextField(default='', verbose_name='текст статьи', blank=False)
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='дата сознания')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    visitors_counter = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    is_published = models.BooleanField(default=False, verbose_name='публикация на сайте')

    # Metadata
    class Meta:
        ordering = ['category']
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    # Methods
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """reverse url of article"""
        return reverse('show_article', kwargs={'article_id': self.pk})
