# Generated by Django 4.0.5 on 2022-10-13 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_coffee_image_coffee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='image_coffee',
            new_name='coffee_image',
        ),
    ]
