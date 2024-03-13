from django.urls import path
from . import views
from django.http import JsonResponse

app_name = "store"

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('view/<int:productId>', views.view, name='view'),
    path('update_item/', views.update_item, name='update_item'),
    path('complete_order/', views.complete_order, name='complete_order')
]