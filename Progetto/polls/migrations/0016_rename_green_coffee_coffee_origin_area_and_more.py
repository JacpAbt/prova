# Generated by Django 4.0.5 on 2022-06-26 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_coffee_green_coffee_coffee_green_coffee_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='green_coffee',
            new_name='origin_area',
        ),
        migrations.RenameField(
            model_name='coffee',
            old_name='green_coffee_2',
            new_name='origin_area_2',
        ),
        migrations.RenameField(
            model_name='coffee',
            old_name='origin',
            new_name='origin_country',
        ),
        migrations.RenameField(
            model_name='coffee',
            old_name='origin_2',
            new_name='origin_country_2',
        ),
    ]
