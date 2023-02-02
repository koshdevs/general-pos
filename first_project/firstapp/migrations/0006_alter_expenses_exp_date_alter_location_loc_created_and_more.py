# Generated by Django 4.1.5 on 2023-02-02 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_location_longitude_alter_expenses_exp_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 11, 10, 26, 519322, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 14, 10, 26, 519322)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='s_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 11, 10, 26, 519322, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='shops',
            name='shop_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 11, 10, 26, 519322, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='p_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 11, 10, 26, 519322, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='t_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 11, 10, 26, 519322, tzinfo=datetime.timezone.utc)),
        ),
    ]
