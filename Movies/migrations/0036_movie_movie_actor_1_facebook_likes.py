# Generated by Django 2.0.13 on 2019-06-19 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0035_auto_20190618_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_actor_1_facebook_likes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
