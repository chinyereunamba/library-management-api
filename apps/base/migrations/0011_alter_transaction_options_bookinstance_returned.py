# Generated by Django 4.2.5 on 2023-09-16 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0010_remove_book__books_available"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transaction",
            options={"ordering": ["-date_borrowed"]},
        ),
        migrations.AddField(
            model_name="bookinstance",
            name="returned",
            field=models.BooleanField(default=False),
        ),
    ]
