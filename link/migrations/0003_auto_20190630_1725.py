# Generated by Django 2.2.2 on 2019-06-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_auto_20190629_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='line_style',
        ),
        migrations.AddField(
            model_name='link',
            name='line_width',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=100),
        ),
    ]