# Generated by Django 4.0.5 on 2022-06-24 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_coffeetypes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeetypes',
            name='taste_profile',
        ),
        migrations.AlterField(
            model_name='coffee',
            name='varieties',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.coffeetypes'),
        ),
    ]
