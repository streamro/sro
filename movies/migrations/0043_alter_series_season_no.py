# Generated by Django 4.1.1 on 2022-11-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0042_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='season_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
