# Generated by Django 5.0 on 2024-01-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
