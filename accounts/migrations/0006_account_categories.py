# Generated by Django 3.1.7 on 2021-04-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210331_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='categories',
            field=models.JSONField(default={}),
        ),
    ]
