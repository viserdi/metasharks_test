# Generated by Django 3.2 on 2022-10-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name='Дата заказа'),
        ),
    ]
