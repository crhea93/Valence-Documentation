# Generated by Django 3.0.2 on 2020-06-10 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_auto_20200610_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cam',
            name='creation_date',
            field=models.CharField(default=datetime.datetime(2020, 6, 10, 20, 32, 30, 976273), max_length=100, verbose_name='Date'),
        ),
    ]