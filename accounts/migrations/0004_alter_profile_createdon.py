# Generated by Django 4.1.2 on 2022-10-15 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_createdon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 13, 42, 31, 834472)),
        ),
    ]
