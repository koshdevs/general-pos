# Generated by Django 4.1.4 on 2023-01-03 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_stocks_p_serial_alter_stocks_p_created_shops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='shop_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 3, 10, 12, 44, 23739, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='p_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 3, 10, 12, 44, 24925, tzinfo=datetime.timezone.utc)),
        ),
    ]
