# Generated by Django 5.0.4 on 2024-05-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("women", "0004_alter_category_options_alter_women_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadFiles",
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
                ("file", models.FileField(upload_to="uploads_model")),
            ],
        ),
    ]
