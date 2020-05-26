# Generated by Django 3.0.6 on 2020-05-23 14:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200523_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.TextField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128),
        ),
    ]
