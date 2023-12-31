# Generated by Django 4.2.5 on 2023-09-13 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_account_first_name_alter_account_last_name"),
        ("base", "0006_alter_bookinstance_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="admin",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="accounts.admin",
            ),
        ),
    ]
