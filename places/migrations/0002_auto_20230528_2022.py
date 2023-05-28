# Generated by Django 4.2.1 on 2023-05-28 20:22

from django.core.management import call_command
from django.db import migrations


def func(apps, schema_editor):
    call_command("loaddata", "data_fixture.json")


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0001_initial"),
    ]

    operations = [migrations.RunPython(func)]
