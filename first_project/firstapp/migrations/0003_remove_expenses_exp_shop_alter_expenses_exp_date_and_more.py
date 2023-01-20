# Generated by Django 4.1.4 on 2023-01-20 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_expenses_exp_date_alter_expenses_exp_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='exp_shop',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 9, 20, 8, 455874, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='s_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 9, 20, 8, 455270, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='shops',
            name='shop_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 9, 20, 8, 453178, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='p_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 9, 20, 8, 454394, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='t_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 9, 20, 8, 456501, tzinfo=datetime.timezone.utc)),
        ),
    ]
