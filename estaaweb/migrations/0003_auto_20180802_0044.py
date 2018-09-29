# Generated by Django 2.0.7 on 2018-08-01 23:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('estaaweb', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hair',
            name='image',
            field=models.ImageField(upload_to='templates/static/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 1, 23, 44, 28, 368740, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='templates/static/img'),
        ),
    ]