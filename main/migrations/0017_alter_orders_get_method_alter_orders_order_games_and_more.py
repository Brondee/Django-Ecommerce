# Generated by Django 4.0.3 on 2022-03-30 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rename_order_info_orders_order_games_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='get_method',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_games',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_method',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_price',
            field=models.CharField(max_length=100),
        ),
    ]
