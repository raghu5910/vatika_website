# Generated by Django 2.1.2 on 2018-11-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='item_description',
            field=models.TextField(default='tasty'),
        ),
    ]
