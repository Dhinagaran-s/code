# Generated by Django 4.1.3 on 2022-11-21 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0002_alter_staffuser_joined_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffuser',
            name='joined_at',
            field=models.DateField(default=datetime.datetime(2022, 11, 21, 14, 54, 16, 527017, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='batch_starting',
            field=models.DateField(default=datetime.datetime(2022, 11, 21, 14, 54, 16, 527259, tzinfo=datetime.timezone.utc)),
        ),
    ]
