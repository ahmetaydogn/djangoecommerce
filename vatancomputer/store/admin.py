from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(ProductDetail)
admin.site.register(Product)
admin.site.register(ItemImage)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(PaymentInformation)