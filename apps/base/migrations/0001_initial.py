# Generated by Django 4.2.5 on 2023-09-09 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0002_student_admin"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=80)),
                ("title", models.CharField(max_length=300)),
                (
                    "isbn",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="ISBN"
                    ),
                ),
                ("date_added", models.DateField(auto_now_add=True)),
                (
                    "quantity",
                    models.IntegerField(default=5, verbose_name="Quantity of books"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("genre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_borrowed",
                    models.DateTimeField(
                        auto_now_add=True,
                        null=True,
                        verbose_name="date the book was borrowed",
                    ),
                ),
                ("date_returned", models.DurationField()),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="accounts.admin",
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="base.book"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="base.genre"
            ),
        ),
    ]
