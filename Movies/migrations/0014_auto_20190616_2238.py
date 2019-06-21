# Generated by Django 2.0.13 on 2019-06-17 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0013_auto_20190616_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_country',
            field=models.CharField(choices=[('CZ', 'Czech Republic'), ('DE', 'Denmark'), ('WE', 'West Germany'), ('CA', 'Cambodia'), ('CA', 'Canada'), ('AR', 'Aruba'), ('AU', 'Australia'), ('BA', 'Bahamas'), ('IN', 'India'), ('SO', 'South Africa'), ('TA', 'Taiwan'), ('UN', 'United Arab Emirates'), ('LI', 'Libya'), ('EG', 'Egypt'), ('PO', 'Poland'), ('BE', 'Belgium'), ('AF', 'Afghanistan'), ('NE', 'New Line'), ('ME', 'Mexico'), ('FR', 'France'), ('GE', 'Georgia'), ('BR', 'Brazil'), ('PE', 'Peru'), ('GE', 'Germany'), ('SO', 'South Korea'), ('RO', 'Romania'), ('SW', 'Switzerland'), ('HO', 'Hong Kong'), ('TU', 'Turkey'), ('PA', 'Pakistan'), ('CA', 'Cameroon'), ('UK', 'UK'), ('CH', 'Chile'), ('PA', 'Panama'), ('SW', 'Sweden'), ('KY', 'Kyrgyzstan'), ('GR', 'Greece'), ('IN', 'Indonesia'), ('TH', 'Thailand'), ('SL', 'Slovakia'), ('RU', 'Russia'), ('OF', 'Official site'), ('FI', 'Finland'), ('NO', 'Norway'), ('DO', 'Dominican Republic'), ('US', 'USA'), ('PH', 'Philippines'), ('IT', 'Italy'), ('JA', 'Japan'), ('HU', 'Hungary'), ('IR', 'Iran'), ('KE', 'Kenya'), ('IS', 'Israel'), ('SL', 'Slovenia'), ('IC', 'Iceland'), ('BU', 'Bulgaria'), ('NE', 'New Zealand'), ('IR', 'Ireland'), ('SP', 'Spain'), ('NI', 'Nigeria'), ('CO', 'Colombia'), ('NE', 'Netherlands'), ('AR', 'Argentina'), ('SO', 'Soviet Union'), ('CH', 'China')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_language',
            field=models.CharField(choices=[('MAN', 'Mandarin'), ('POL', 'Polish'), ('SPA', 'Spanish'), ('MON', 'Mongolian'), ('ITA', 'Italian'), ('IND', 'Indonesian'), ('HIN', 'Hindi'), ('KOR', 'Korean'), ('PER', 'Persian'), ('CAN', 'Cantonese'), ('JAP', 'Japanese'), ('BOS', 'Bosnian'), ('ENG', 'English'), ('MAY', 'Maya'), ('KAN', 'Kannada'), ('GRE', 'Greek'), ('HEB', 'Hebrew'), ('GER', 'German'), ('DZO', 'Dzongkha'), ('FRE', 'French'), ('ARA', 'Aramaic'), ('RUS', 'Russian'), ('DAR', 'Dari'), ('ZUL', 'Zulu'), ('URD', 'Urdu'), ('ICE', 'Icelandic'), ('DAN', 'Danish'), ('PAN', 'Panjabi'), ('ABO', 'Aboriginal'), ('ROM', 'Romanian'), ('SLO', 'Slovenian'), ('FIL', 'Filipino'), ('SWE', 'Swedish'), ('TAM', 'Tamil'), ('NON', 'None'), ('NOR', 'Norwegian'), ('DUT', 'Dutch'), ('CHI', 'Chinese'), ('THA', 'Thai'), ('TEL', 'Telugu'), ('SWA', 'Swahili'), ('CZE', 'Czech'), ('POR', 'Portuguese'), ('VIE', 'Vietnamese'), ('KAZ', 'Kazakh'), ('ARA', 'Arabic'), ('HUN', 'Hungarian')], max_length=200, null=True),
        ),
    ]
