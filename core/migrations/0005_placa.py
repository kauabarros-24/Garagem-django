# Generated by Django 5.0.2 on 2024-04-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_modelo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Placa",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("placa", models.CharField(max_length=15)),
            ],
        ),
    ]
