# Generated by Django 4.0.3 on 2022-03-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_check_bill_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='bill_id',
            field=models.CharField(max_length=500, null=True),
        ),
    ]