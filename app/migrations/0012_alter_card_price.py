# Generated by Django 4.1.7 on 2023-05-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_card_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
