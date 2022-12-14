# Generated by Django 4.1.1 on 2022-11-14 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0038_alter_episode_season_delete_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField(default=True)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.show')),
            ],
        ),
        migrations.AlterField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.season'),
        ),
    ]
