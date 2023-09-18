from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from django.core.signals import request_finished
from django.dispatch import receiver
from apps.accounts.models import Account, Admin, Student
import uuid
from datetime import date, datetime

# Create your models here.


class Author(models.Model):
    author = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return self.author


class Genre(models.Model):
    """Category books belong"""
    genre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.genre


class Book(models.Model):
    """Model Representing books in the Library"""

    author = models.CharField(max_length=80, blank=False, null=False)
    title = models.CharField(max_length=300, blank=False, null=False)
    isbn = models.CharField(verbose_name="ISBN",
                            max_length=20, blank=True, null=True)
    summary = models.TextField(blank=True)
    date_added = models.DateField(auto_now_add=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(verbose_name="Quantity of books", default=5)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    @property
    def books_available(self):
        books_available = self.quantity
        return books_available

    @books_available.setter
    def set_books_available(self, value):
        books_available = value


# LOAN_STATUS = [("borrowed", "Borrowed"), ("returned", "Returned")]

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        blank=True,
        help_text="Unique ID for this particular book across whole library",
    )
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    returned = models.BooleanField(default=False)
    date_returned = models.DateField(blank=True, null=True)

    LOAN_STATUS = (
        ("o", "On loan"),
        ("a", "Available"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="a",
        help_text="Book availability",
    )

    def save(self, *args, **kwargs):
        if self.returned:
            self.date_returned = date.today()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["book"]

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.book}"


class Transaction(models.Model):
    """Model enables the provision of ticket to a student when a book is borrowed"""

    admin = models.ForeignKey(
        Admin, on_delete=models.DO_NOTHING, blank=True, null=True)
    ticket = models.CharField(max_length=255, default="")
    book = models.ForeignKey(BookInstance, on_delete=models.DO_NOTHING)
    date_borrowed = models.DateTimeField(
        verbose_name="date the book was borrowed",
        auto_now_add=True,
        blank=True,
        null=True,
    )

    approved = models.BooleanField(default=False)
    due_back = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.admin:
            self.approved = True

        self.ticket = self.book.id

        super().save(*args, **kwargs)

    def __str__(self,):
        return f'{self.book}'

    class Meta:
        ordering = ['-date_borrowed']


@receiver(post_save, sender=BookInstance)
def create_transaction(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(book=instance)
