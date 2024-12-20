# Generated by Django 5.1.2 on 2024-12-04 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kyc", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2024, 12, 4, 16, 47, 43, 347467, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="customer",
            name="first_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="customer",
            name="last_name",
            field=models.CharField(max_length=255),
        ),
    ]
