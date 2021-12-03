# Generated by Django 3.2.9 on 2021-12-03 09:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0019_auto_20211203_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='recipes',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 3, 10, 6, 18, 320780)),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.user'),
        ),
    ]
