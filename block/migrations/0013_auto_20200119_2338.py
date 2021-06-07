# Generated by Django 2.2.6 on 2020-01-19 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0012_auto_20191023_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='shape',
            field=models.CharField(choices=[('neutral', 'rectangle'), ('positive', 'rounded-circle'), ('negative', 'hexagon'), ('positive strong', 'rounded-circle-strong'), ('negative strong', 'hexagon strong'), ('ambivalent', 'hexagon rounded-circle'), ('negative weak', 'hexagon weak'), ('positive weak', 'rounded-circle-weak')], max_length=100),
        ),
    ]
