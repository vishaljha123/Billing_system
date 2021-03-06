# Generated by Django 3.0.6 on 2020-05-21 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200521_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
        migrations.CreateModel(
            name='order_by_date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
            ],
            options={
                'ordering': ['ordered_date'],
            },
        ),
    ]
