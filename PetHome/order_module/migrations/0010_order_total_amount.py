# Generated by Django 4.2.3 on 2024-04-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0009_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.IntegerField(blank=True, default=0, verbose_name='مجموع'),
            preserve_default=False,
        ),
    ]
