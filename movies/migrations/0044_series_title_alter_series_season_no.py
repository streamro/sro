# Generated by Django 4.1.1 on 2022-11-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0043_alter_series_season_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='season_no',
            field=models.IntegerField(null=True),
        ),
    ]
