# Generated by Django 2.2.3 on 2019-08-09 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0023_auto_20190807_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='views',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateField(default=datetime.date(2019, 8, 9)),
        ),
    ]
