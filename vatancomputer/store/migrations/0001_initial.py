# Generated by Django 4.2.7 on 2024-03-04 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('batteryType', models.CharField(max_length=50)),
                ('batteryCellCount', models.CharField(max_length=50)),
                ('security', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('ramType', models.CharField(max_length=50)),
                ('graphicsCardChipsetBrand', models.CharField(max_length=50)),
                ('graphicsCardChipset', models.CharField(max_length=50)),
                ('graphicsCardMemoryType', models.CharField(max_length=50)),
                ('graphicsCardMemory', models.CharField(max_length=50)),
                ('graphicsCardType', models.CharField(max_length=50)),
                ('diskCapacity', models.CharField(max_length=50)),
                ('diskType', models.CharField(max_length=50)),
                ('power', models.CharField(max_length=50)),
                ('multimediaHeadphoneOutput', models.CharField(max_length=50)),
                ('multimediaFeatures', models.CharField(max_length=50)),
                ('multimediaCamera', models.CharField(max_length=50)),
                ('multimediaFingerprintReader', models.CharField(max_length=50)),
                ('keyboard', models.CharField(max_length=50)),
                ('monitor', models.CharField(max_length=50)),
                ('operatingSystem', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('fastCharging', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=50)),
                ('guarantee', models.CharField(max_length=50)),
                ('processorType', models.CharField(max_length=50)),
                ('processorGen', models.CharField(max_length=50)),
                ('processorTech', models.CharField(max_length=50)),
                ('processorNum', models.CharField(max_length=50)),
                ('processorSpeed', models.CharField(max_length=50)),
                ('processorCache', models.CharField(max_length=50)),
                ('processorCore', models.CharField(max_length=50)),
                ('screenSize', models.CharField(max_length=50)),
                ('screenrRefreshRate', models.CharField(max_length=50)),
                ('screenFeatures', models.CharField(max_length=50)),
                ('screenResolution', models.CharField(max_length=50)),
                ('screenIPS', models.CharField(max_length=50)),
                ('screenFullHD', models.CharField(max_length=50)),
                ('screenHD', models.CharField(max_length=50)),
                ('screenTN', models.CharField(max_length=50)),
                ('screenTouch', models.CharField(max_length=50)),
                ('connectionSpecificationUSB20', models.CharField(max_length=50)),
                ('connectionSpecificationUSB32', models.CharField(max_length=50)),
                ('connectionSpecificationUSBTypeC', models.CharField(max_length=50)),
                ('connectionSpecificationBluetoothTech', models.CharField(max_length=50)),
                ('connectionSpecificationEtherner', models.CharField(max_length=50)),
                ('connectionSpecificationWiFi', models.CharField(max_length=50)),
                ('connectionSpecificationHDMI', models.CharField(max_length=50)),
                ('connectionSpecificationCardSlot', models.CharField(max_length=50)),
                ('connectionSpecificationBluetooth', models.CharField(max_length=50)),
                ('illuminatedKeyboard', models.CharField(max_length=50)),
                ('intendedUse1', models.CharField(max_length=50)),
                ('intendedUse2', models.CharField(max_length=50)),
                ('manufacturerPartNumber', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
                ('width', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('address_optional', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('productDetail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.productdetail')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
