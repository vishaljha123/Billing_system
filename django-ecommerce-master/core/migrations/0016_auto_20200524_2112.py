# Generated by Django 3.0.6 on 2020-05-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200523_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tests',
            field=models.TextField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
