# Generated by Django 3.2.4 on 2022-01-05 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000000)),
                ('date_sent', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
