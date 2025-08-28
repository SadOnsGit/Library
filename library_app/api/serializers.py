from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField

from books.models import Book

class BookSerializer(ModelSerializer):
    published_author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        fields = ('__all__')
        model = Book
