# Generated by Django 4.0.3 on 2022-03-31 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_orders_get_method_alter_orders_order_games_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='games_ids',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
