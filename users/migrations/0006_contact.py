# Generated by Django 2.2.6 on 2020-02-01 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_cam_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacter', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]