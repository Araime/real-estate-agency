# Generated by Django 2.2.20 on 2021-06-29 12:54

from django.db import migrations


def update_new_buildings_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(update_new_buildings_field, move_backward)
    ]