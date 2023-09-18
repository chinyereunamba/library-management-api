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
    admin_name = serializers.CharField(source='admin', read_only=True)
    userId = serializers.IntegerField(source='book.user.id')
    first_name = serializers.CharField(source='book.user.first_name')
    last_name = serializers.CharField(source='book.user.last_name')

    class Meta:
        model = Transaction
        fields = "__all__"


class BookInstanceSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(
        source='book.title', required=False, read_only=True)

    class Meta:
        model = BookInstance
        fields = '__all__'
        read_only_fields = ['id', 'book_title', 'status']

    def create(self, validated_data):
        status = validated_data.get('status')
        book = validated_data.get('book')
        user = validated_data.get('user')

        book_instance = BookInstance.objects.create(**validated_data)
        return book_instance
    