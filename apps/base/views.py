from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


from .models import Book, Genre, Transaction
from .serializer import BookSerializer, GenreSerializer, TransactionSerializer

# Create your views here.

class BookViews(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

class GenreView(ModelViewSet):
    queryset = Genre
    serializer_class = GenreSerializer
    lookup_field = 'pk'
    
class TransactionView(ListCreateAPIView):
    queryset = Transaction
    serializer_class = TransactionSerializer