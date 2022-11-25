# Generated by Django 4.1.1 on 2022-09-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_remove_movie_is_main_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('Action & Adventure', 'Action & Adventure'), ('Comedies', 'Comedies'), ('Drama', 'Drama'), ('Blockbuster Movies', 'Blockbuster Movies')], max_length=100),
        ),
    ]