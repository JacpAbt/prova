# Generated by Django 4.0.5 on 2022-06-26 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_coffee_url_to_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='origin_1',
            new_name='origin',
        ),
        migrations.RenameField(
            model_name='coffee',
            old_name='process_1',
            new_name='process',
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='origin_2',
        ),
        migrations.RemoveField(
            model_name='coffee',
            name='process_2',
        ),
    ]
