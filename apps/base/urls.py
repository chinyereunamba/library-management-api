from django.urls import path
from .views import *


urlpatterns = [
    path("", CreateBook.as_view(), name='books')
]