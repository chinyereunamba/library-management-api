# Generated by Django 4.2.5 on 2023-09-09 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_book_options_remove_transaction_date_returned_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinstance",
            name="imprint",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
