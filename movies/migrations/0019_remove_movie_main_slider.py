# Generated by Django 4.1.1 on 2022-09-22 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_movie_main_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='main_slider',
        ),
    ]