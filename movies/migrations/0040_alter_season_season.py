# Generated by Django 4.1.1 on 2022-11-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0039_season_alter_episode_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
