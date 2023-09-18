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
    path(
        "genre/", GenreView.as_view({"post": "create", "get": "list"}), name="genre"),
    path('borrow/',
         BookInstanceView.as_view(
             {
                 'post': 'create',
                 "get": 'list',
             }
         ), name='book-instance'),
    path('borrow/<slug:id>/',
         BookInstanceView.as_view({"patch": 'partial_update', 'get':'retrieve'})),
    path(
        'ticket/', TicketView.as_view({'get': 'list', 'patch': "partial_update"})),
    path('ticket/<slug:ticket>/', TicketView.as_view({'patch': "partial_update", 'get':"retrieve"})),
    path('users/', StudentView.as_view()),
    path('users/<int:user>/', StudentDetailView.as_view()),
    path('admin/<int:user>/', AdminUsers.as_view()),

]
