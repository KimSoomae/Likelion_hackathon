# Generated by Django 2.2.3 on 2019-07-31 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0013_remove_board_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='writer',
            field=models.CharField(default='', max_length=100),
        ),
    ]