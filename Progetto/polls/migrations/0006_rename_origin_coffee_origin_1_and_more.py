# Generated by Django 4.0.5 on 2022-06-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_merchant_merchant_name_user_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='origin',
            new_name='origin_1',
        ),
        migrations.RenameField(
            model_name='coffee',
            old_name='producer_id',
            new_name='seller_id',
        ),
        migrations.AddField(
            model_name='coffee',
            name='origin_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='process_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='process_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='seller',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='tasting_notes',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='coffee',
            name='varieties',
            field=models.CharField(max_length=200, null=True),
        ),
    ]