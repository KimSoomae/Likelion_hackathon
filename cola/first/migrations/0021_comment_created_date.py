# Generated by Django 2.2.3 on 2019-08-04 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0020_remove_comment_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateField(default=datetime.date(2019, 8, 4)),
        ),
    ]