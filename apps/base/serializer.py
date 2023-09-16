from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'author', 'isbn', 'summary',
                  'genre', 'quantity', 'books_available']
        

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["genre"]


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
        depth = 2


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = '__all__'
