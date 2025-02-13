# Generated by Django 4.1.5 on 2023-03-20 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=500)),
                ('user', models.CharField(max_length=500)),
                ('msg', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
