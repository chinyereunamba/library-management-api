from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["genre"]


class TransactionSerializer(serializers.ModelSerializer):
    book = serializers.RelatedField(source="transaction.book", read_only=True)

    class Meta:
        model = Transaction
        fields = ["__all__"]


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = '__all__'