# Generated by Django 3.2.4 on 2022-01-05 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientMessages',
            new_name='ClientMessage',
        ),
    ]
