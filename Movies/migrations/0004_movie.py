# Generated by Django 2.0.13 on 2019-06-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0003_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id_movie', models.AutoField(primary_key=True, serialize=False)),
                ('movie_title', models.CharField(max_length=200)),
            ],
        ),
    ]