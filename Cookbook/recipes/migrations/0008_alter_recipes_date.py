# Generated by Django 3.2.9 on 2021-12-01 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipes_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 1, 15, 41, 0, 343175)),
        ),
    ]