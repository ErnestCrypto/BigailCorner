# Generated by Django 3.2.8 on 2021-10-17 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_orders', models.CharField(max_length=10)),
                ('date_ordered', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StockTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_price', models.CharField(max_length=30)),
                ('date_bought', models.DateField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_initial_stock', models.CharField(max_length=20)),
                ('date_stock_was_filled', models.CharField(max_length=10)),
                ('number_of_remaining_stock', models.CharField(max_length=20)),
                ('stocktransaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BigailsCornerApp.stocktransaction')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_number_of_products', models.CharField(max_length=20)),
                ('date_products_were_purchased', models.DateField(max_length=10)),
                ('products_left_in_store', models.CharField(max_length=20)),
                ('stock', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BigailsCornerApp.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Orderline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_orderlines', models.CharField(max_length=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BigailsCornerApp.order')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BigailsCornerApp.product')),
            ],
        ),
    ]