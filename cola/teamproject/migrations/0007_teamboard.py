# Generated by Django 2.2.3 on 2019-07-31 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamproject', '0006_auto_20190730_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('img', models.ImageField(upload_to='teamboard/')),
                ('writer', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
