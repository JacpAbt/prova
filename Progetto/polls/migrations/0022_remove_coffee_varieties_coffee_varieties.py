# Generated by Django 4.0.5 on 2022-06-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_alter_coffee_process'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='varieties',
        ),
        migrations.AddField(
            model_name='coffee',
            name='varieties',
            field=models.ManyToManyField(to='polls.coffeeplanttype'),
        ),
    ]