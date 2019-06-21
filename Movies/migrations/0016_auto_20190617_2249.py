# Generated by Django 2.0.13 on 2019-06-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0015_auto_20190617_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id_actor', models.AutoField(primary_key=True, serialize=False)),
                ('actor_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_aspect_ratio',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_budget',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_color',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_director_facebook_likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_duration',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_facebook_likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_gross',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_imdb_link',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_imdb_score',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_language',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_num_voted_users',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_year',
        ),
    ]