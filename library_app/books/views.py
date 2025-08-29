from django.views.generic import ListView

from .models import Book


class BookView(ListView):
    model = Book
    template_name = 'books/index.html'

    def get_queryset(self):
        books = Book.objects.select_related('published_author').prefetch_related('author', 'category').all()
        query = self.request.GET.get('q')
        if query:
            return books.filter(name__icontains=query)
        return books