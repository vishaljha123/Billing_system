# Generated by Django 3.0.6 on 2020-05-24 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20200525_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='ordered_date',
        ),
    ]
