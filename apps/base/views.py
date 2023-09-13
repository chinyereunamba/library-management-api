from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView, GenericAPIView, CreateAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .models import (
    Book,
    Genre,
    Transaction,
    BookInstance
)

from .serializer import (
    BookSerializer,
    GenreSerializer,
    TransactionSerializer,
    BookInstanceSerializer
)

# Create your views here.


class BookViews(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'


class GenreView(ModelViewSet):
    queryset = Genre
    serializer_class = GenreSerializer
    lookup_field = 'pk'



# def borrow_book(request, pk):
#     serializer = BookInstanceSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         response = serializer.data

class BookInstanceView(CreateAPIView):
    serializer_class = BookInstanceSerializer
    queryset = BookInstance
    permission_classes = [AllowAny,]