# Generated by Django 4.2.3 on 2023-07-31 06:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0002_alter_transaction_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2023, 7, 31, 6, 26, 33, 329271, tzinfo=datetime.timezone.utc), max_length=19),
        ),
    ]
