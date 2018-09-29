# Generated by Django 2.0.7 on 2018-08-03 05:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('estaaweb', '0005_auto_20180802_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hair',
            name='image',
            field=models.ImageField(upload_to='estaaweb/static/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 3, 5, 34, 53, 610851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='estaaweb/static/img'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(upload_to='estaaweb/static/img'),
        ),
    ]