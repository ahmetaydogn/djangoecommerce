# Generated by Django 4.2.7 on 2024-03-13 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_paymentinformation_card_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentinformation',
            name='payment_method',
        ),
    ]
