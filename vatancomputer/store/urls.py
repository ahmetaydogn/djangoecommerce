from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('view/<int:productId>', views.view, name='view')
]