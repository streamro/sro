# Generated by Django 4.1.1 on 2022-11-12 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0029_show_delete_serials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.show')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('episode_number', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.season')),
            ],
        ),
    ]