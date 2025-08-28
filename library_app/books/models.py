from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'авторы'


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'


class Book(models.Model):
    name = models.CharField(
        max_length=50
    )
    author = models.ManyToManyField(
        Author,
        related_name='books'
    )
    category = models.ManyToManyField(
        Category,
        related_name='category_books'
    )
    published_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='published_books'
    )
    release_date = models.DateField(
        verbose_name='Дата выхода книги',
    )
    image = models.ImageField(
        upload_to='books/', null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'книги'
