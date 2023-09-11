from django.db import models
from apps.accounts.models import Account, Admin
import uuid

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
    isbn = models.CharField(verbose_name="ISBN", max_length=20, blank=True, null=True)
    summary = models.TextField(blank=True)
    date_added = models.DateField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(verbose_name="Quantity of books", default=5)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


# LOAN_STATUS = [("borrowed", "Borrowed"), ("returned", "Returned")]


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library",
    )
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200, blank=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.id} ({self.book.title})"


class Transaction(models.Model):
    """Model enables the provision of ticket to a student when a book is borrowed"""

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(BookInstance, on_delete=models.DO_NOTHING)
    date_borrowed = models.DateTimeField(
        verbose_name="date the book was borrowed",
        auto_now_add=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.book} was borrowed by {self.user}"
