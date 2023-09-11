from django.urls import path
from .views import *


urlpatterns = [
    # path("", CreateBook.as_view(), name='books'),
    path(
        "",
        BookViews.as_view(
            {
                "post": "create",
                "get": "list",
            }
        ),
        name="books",
    ),
    path(
        "book/<int:pk>/",
        BookViews.as_view(
            {
                "put": "update",
                "delete": "destroy",
                "get": "retrieve",
                "patch": "partial_update",
            }
        ),
    ),
    path("genre/", GenreView.as_view({"post": "create", "get": "list"}), name="genre"),
    path("transactions/", TransactionView.as_view(), name="transaction"),
]
