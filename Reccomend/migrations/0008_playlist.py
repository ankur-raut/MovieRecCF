# Generated by Django 4.1.3 on 2023-02-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reccomend', '0007_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('movies', models.ManyToManyField(to='Reccomend.movie')),
            ],
        ),
    ]