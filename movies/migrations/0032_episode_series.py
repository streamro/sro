# Generated by Django 4.1.1 on 2022-11-12 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0031_episode_image_episode_episode_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='series',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='movies.show'),
        ),
    ]
