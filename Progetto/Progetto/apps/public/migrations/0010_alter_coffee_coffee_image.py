# Generated by Django 4.0.5 on 2022-12-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0009_alter_coffee_coffee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='coffee_image',
            field=models.ImageField(blank=True, null=True, upload_to='theme/assets/img/Coffee/'),
        ),
    ]
