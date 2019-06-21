# Generated by Django 2.0.13 on 2019-06-19 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0026_auto_20190618_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_aspect_ratio',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_imdb_score',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
    ]