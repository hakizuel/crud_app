# Generated by Django 5.0.6 on 2024-05-26 06:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Students",
            new_name="Student",
        ),
    ]
