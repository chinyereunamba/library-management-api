from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'summary',
                  'genre', 'quantity', 'books_available']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["genre"]


class TransactionSerializer(serializers.ModelSerializer):
    date_borrowed = serializers.DateTimeField(format="%d-%h-%y %H:%M")
    due_back = serializers.DateField(format='%d-%h-%y')
    book = serializers.CharField()
    admin = serializers.CharField()
    first_name = serializers.CharField(source='book.user.first_name')
    last_name = serializers.CharField(source='book.user.last_name')

    class Meta:
        model = Transaction
        fields = "__all__"


class BookInstanceSerializer(serializers.ModelSerializer):
    book = serializers.CharField()
    class Meta:
        model = BookInstance
        fields = '__all__'
