# Generated by Django 3.0.6 on 2020-05-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200523_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='media_root/images/'),
        ),
    ]
