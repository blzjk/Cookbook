# Generated by Django 3.2.9 on 2021-11-30 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20211130_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 30, 18, 34, 24, 581308)),
        ),
    ]