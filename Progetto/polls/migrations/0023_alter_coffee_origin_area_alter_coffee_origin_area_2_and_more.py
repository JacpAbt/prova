# Generated by Django 4.0.5 on 2022-06-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_remove_coffee_varieties_coffee_varieties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='origin_area',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='origin_area_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='origin_country_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='producer_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]