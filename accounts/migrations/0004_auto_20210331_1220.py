# Generated by Django 3.1.7 on 2021-03-31 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210331_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
