# Generated by Django 5.1.1 on 2024-09-14 08:08

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_rom', models.CharField(choices=[('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB'), ('128GB', '128GB'), ('256GB', '256GB'), ('512GB', '512GB'), ('1TB', '1TB')], max_length=100)),
                ('product_ram', models.CharField(choices=[('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB')], max_length=100)),
                ('product_camera', models.TextField()),
                ('product_battery', models.TextField()),
                ('product_processor', models.TextField()),
                ('product_os', models.TextField()),
                ('product_connectivity', models.TextField()),
                ('product_colors', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('distributor_id', models.AutoField(primary_key=True, serialize=False)),
                ('distributor_name', models.CharField(max_length=100)),
                ('distributor_address', models.TextField(verbose_name='')),
                ('distributor_brands', models.ManyToManyField(related_name='brands_distributor', to='smart_centre.brands')),
            ],
        ),
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('product_name_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_sku', models.CharField(max_length=100)),
                ('prodyuct_specs', models.TextField()),
                ('products_rdp', models.FloatField()),
                ('product_rrp', models.FloatField()),
                ('product_wholesale_price', models.FloatField(null=True)),
                ('retail', models.BooleanField(default=True)),
                ('launch', models.DateField(default=django.utils.timezone.now)),
                ('eol_date', models.DateTimeField(default=datetime.datetime(2025, 3, 13, 11, 8, 36, 364301))),
                ('product_image', models.ImageField(default='product.jpg', upload_to='smart_products')),
                ('product_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smart_centre.brands')),
            ],
        ),
        migrations.CreateModel(
            name='StocksList',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('device_serial1', models.CharField(max_length=100)),
                ('device_serial2', models.CharField(max_length=100)),
                ('device_stock_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('device_stock_stage', models.CharField(choices=[('Distributor', 'Distributor'), ('Retailer', 'Retailer')], default='Distributor', max_length=100)),
                ('device_added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('device_specs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_specs', to='smart_centre.productname')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceSales',
            fields=[
                ('device_sale_id', models.AutoField(primary_key=True, serialize=False)),
                ('profit', models.FloatField()),
                ('stage', models.CharField(choices=[('cart', 'cart'), ('sold', 'sold'), ('disputed', 'disputed'), ('returned', 'returned')], max_length=100)),
                ('sales_date', models.DateField(default=datetime.datetime(2024, 9, 14, 8, 8, 36, 364301, tzinfo=datetime.timezone.utc), verbose_name='Sales Date')),
                ('disputed_date', models.DateField(null=True, verbose_name='Disputed Date')),
                ('returned_date', models.DateField(null=True, verbose_name='Returned Date')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_id', models.CharField(max_length=100)),
                ('customer_phone', models.CharField(max_length=100)),
                ('customer_address', models.TextField()),
                ('warranty', models.ImageField(default='warranty.jpg', upload_to='smart_products_warranty')),
                ('warranty_expiry_date', models.DateTimeField(null=True)),
                ('sold_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Sales Man')),
                ('device_product_spec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smart_centre.stockslist')),
            ],
        ),
    ]
