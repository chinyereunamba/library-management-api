# Generated by Django 4.2.5 on 2023-09-13 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0009_book__books_available"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="_books_available",
        ),
    ]
