# Generated by Django 4.0.3 on 2022-03-31 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_orders_games_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_from',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
