# Generated by Django 4.1.7 on 2023-03-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery1', '0004_remove_gallery_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('user', models.CharField(default='admin', max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(upload_to='video/%y')),
            ],
        ),
    ]