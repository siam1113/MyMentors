# Generated by Django 3.2.9 on 2022-01-18 19:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ask', '0009_alter_ask_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='datetime',
            field=models.DateTimeField(auto_now=True, verbose_name=datetime.datetime(2022, 1, 18, 19, 53, 17, 33764, tzinfo=utc)),
        ),
    ]