# Generated by Django 4.1.7 on 2023-03-12 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery1', '0002_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='category',
        ),
    ]
