# Generated by Django 5.0.6 on 2024-12-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_profile_old_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
