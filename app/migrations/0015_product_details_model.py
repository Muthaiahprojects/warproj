# Generated by Django 4.1.7 on 2023-05-29 05:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_card_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='model',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
