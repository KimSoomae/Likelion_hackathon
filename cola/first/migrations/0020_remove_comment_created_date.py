# Generated by Django 2.2.3 on 2019-08-04 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0019_comment_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_date',
        ),
    ]
