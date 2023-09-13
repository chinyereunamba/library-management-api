from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Transaction

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", 'author', "quantity", "genre"]
    search_fields = ["title", "genre", 'author']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ["book", "admin"]
    search_fields = ["book", "user"]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'book']
    readonly_fields = ['id']

admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Genre)
admin.site.register(Author)
