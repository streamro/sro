# Generated by Django 4.1.1 on 2022-09-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_remove_movie_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='main_slider',
            field=models.ImageField(blank=True, upload_to='main_slider/'),
        ),
    ]