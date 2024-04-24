# Generated by Django 5.0.2 on 2024-04-24 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_placa"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "cor",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="cores", to="core.cor"),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="marcas", to="core.marca"
                    ),
                ),
                (
                    "modelo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="modelos", to="core.modelo"
                    ),
                ),
                (
                    "placa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="placas", to="core.placa"
                    ),
                ),
            ],
        ),
    ]
