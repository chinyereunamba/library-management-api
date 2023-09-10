from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView



from .models import Book
from .serializer import BookSerializer
# Create your views here.

class CreateBook(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
