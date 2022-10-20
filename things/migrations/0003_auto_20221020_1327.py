# Generated by Django 2.2.12 on 2022-10-20 13:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_auto_20221020_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='thing',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Value must be bigger than 0!'), django.core.validators.MaxValueValidator(100, message='Value must be less than 100!')]),
        ),
    ]
