# Generated by Django 2.0.13 on 2019-06-19 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0027_auto_20190618_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_color',
            field=models.CharField(choices=[('C', 'Color'), ('BW', 'Black And White')], max_length=2, null=True),
        ),
    ]