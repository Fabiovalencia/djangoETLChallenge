# Generated by Django 2.0.13 on 2019-06-16 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0004_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_imdb_link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]