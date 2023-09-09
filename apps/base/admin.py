from django.contrib import admin
from .models import Author, Book, Genre, Transaction

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ["title",'quantity', "genre"]
    search_fields = ["title", "genre"]

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'admin']
    search_fields = ['book', 'user']

admin.site.register(Book, BookAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Genre)
admin.site.register(Author)
