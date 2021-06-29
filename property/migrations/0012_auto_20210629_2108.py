# Generated by Django 2.2.20 on 2021-06-29 17:08

from django.db import migrations


def connect_flats_with_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        print(owner)
        flats = Flat.objects.filter(owner=owner.owner)
        owner.owned_flats.set(flats, clear=True)


def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.owned_flats.set([], clear=True)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20210629_2107'),
    ]

    operations = [
        migrations.RunPython(connect_flats_with_owners, move_backward)
    ]