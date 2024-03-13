# Generated by Django 4.2.7 on 2024-03-13 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_orderitem_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=6)),
                ('card_number', models.CharField(max_length=19)),
                ('expires_end', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=3)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='payment_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.paymentinformation'),
        ),
    ]