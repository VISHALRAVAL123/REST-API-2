# Generated by Django 4.2.2 on 2023-06-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]
