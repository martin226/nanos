# Generated by Django 4.0.4 on 2022-05-25 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URLShorten",
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
                ("url", models.URLField(max_length=255)),
                ("short_url", models.CharField(max_length=8, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="View",
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
                ("viewed_at", models.DateTimeField(auto_now_add=True)),
                ("country", models.CharField(max_length=255, null=True)),
                ("ip", models.GenericIPAddressField(null=True)),
                ("referrer", models.CharField(max_length=255, null=True)),
                ("device", models.CharField(max_length=255, null=True)),
                (
                    "short_url",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="views",
                        to="api.urlshorten",
                    ),
                ),
            ],
        ),
    ]
