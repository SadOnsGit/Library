from django.views.generic import ListView

from .models import Book


class BookView(ListView):
    model = Book
    template_name = 'books/index.html'
