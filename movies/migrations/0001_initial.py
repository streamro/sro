# Generated by Django 4.1.1 on 2022-09-19 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=105)),
                ('tags', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='photos/')),
                ('video', models.URLField()),
                ('imdb', models.IntegerField()),
                ('category', models.CharField(choices=[('Action & Adventure', 'Action & Adventure'), ('Comedies', 'Comedies'), ('Drama', 'Drama'), ('Blockbuster Movies', 'Blockbuster Movies')], max_length=100)),
                ('is_favorite', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('date_published', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
