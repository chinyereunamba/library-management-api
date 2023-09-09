from django.db import models
from apps.accounts.models import Account, Admin

# Create your models here.


class Author(models.Model):
    author = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return self.author


class Genre(models.Model):
    genre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.genre


class Book(models.Model):
    author = models.CharField(max_length=80, blank=False, null=False)
    title = models.CharField(max_length=300, blank=False, null=False)
    isbn = models.CharField(verbose_name="ISBN", max_length=20, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Quantity of books", default=5)


class Transaction(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    date_borrowed = models.DateTimeField(
        verbose_name="date the book was borrowed",
        auto_now_add=True,
        blank=True,
        null=True,
    )
    date_returned = models.DurationField()

    def __str__(self):
        return f'{self.book} was borrowed by {self.user}'
