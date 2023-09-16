from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, GenericAPIView, CreateAPIView, ListAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
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

from apps.accounts.models import Student
from apps.accounts.serializers import StudentSerializer

# Create your views here.


class BookViews(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'


class GenreView(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'


class BookInstanceView(ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    permission_classes = [AllowAny]

class TicketView(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]

class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]