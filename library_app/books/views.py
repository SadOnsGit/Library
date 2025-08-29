from django.views.generic import ListView

from .models import Book


class BookView(ListView):
    model = Book
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.select_related('published_author').prefetch_related('author', 'category')
