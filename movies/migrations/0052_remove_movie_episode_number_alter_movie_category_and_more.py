# Generated by Django 4.1.1 on 2022-11-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0051_movie_episode_number_alter_movie_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='episode_number',
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('Action & Adventure', 'Action & Adventure'), ('Comedies', 'Comedies'), ('Drama', 'Drama'), ('Blockbuster Movies', 'Blockbuster Movies'), ('Popular Movies', 'Popular Movies'), ('Cartoons', 'Cartoons'), ('Documentaries', 'Documentaries')], max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tags',
            field=models.CharField(choices=[('Exciting Movies', 'Exciting Movies'), ('Critically Acclaimed Films', 'Critically Acclaimed Films'), ('Familiar Favorites', 'Familiar Favorites')], max_length=50),
        ),
        migrations.AlterField(
            model_name='show',
            name='category',
            field=models.CharField(choices=[('Documentary Films', 'Documentary Films'), ('Watch In One Night', 'Watch In One Night'), ('Popular Documentaries', 'Popular Documentaries'), ('Best Of International Shows', 'Best Of International Shows'), ('Popular Shows', 'Popular Shows'), ('Familiar TV Favorites', 'Familiar TV Favorites')], max_length=100),
        ),
    ]