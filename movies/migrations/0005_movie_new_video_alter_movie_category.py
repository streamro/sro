# Generated by Django 4.1.1 on 2022-09-20 11:24

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_year_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='new_video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('Action & Adventure', 'Action & Adventure'), ('Comedies', 'Comedies'), ('Drama', 'Drama'), ('Blockbuster Movies', 'Blockbuster Movies'), ('Top-10', 'Top-10')], max_length=100),
        ),
    ]
