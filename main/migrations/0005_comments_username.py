# Generated by Django 4.0.3 on 2022-03-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_price_day_alter_product_price_week_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='username',
            field=models.CharField(default='User', max_length=150),
        ),
    ]
