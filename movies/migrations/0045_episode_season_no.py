# Generated by Django 4.1.1 on 2022-11-15 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0044_series_title_alter_series_season_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='season_no',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.series'),
        ),
    ]
