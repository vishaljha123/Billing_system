# Generated by Django 3.0.6 on 2020-05-24 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_order_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_date',
        ),
        migrations.AddField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 17, 43, 34, 307987, tzinfo=utc)),
        ),
    ]
