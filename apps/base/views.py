from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser



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

from apps.accounts.models import Student, Admin
from apps.accounts.serializers import StudentSerializer, AdminProfile

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
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save()
        return super().perform_create(serializer)
    


class TicketView(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]
    lookup_field = 'ticket'

    def perform_update(self, serializer):
        instance = serializer.save()
        return super().perform_update(serializer)

class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

class StudentDetailView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    lookup_field = 'user'

class AdminUsers(RetrieveAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminProfile
    permission_classes = [AllowAny]
    lookup_field = 'user'