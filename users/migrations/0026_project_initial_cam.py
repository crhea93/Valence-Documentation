# Generated by Django 2.2.6 on 2020-04-09 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20200404_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Initial_CAM',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]