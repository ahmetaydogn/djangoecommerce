from django.shortcuts import render
from . import models

# Create your views here.

def store(request):
    products = models.Product.objects.all()
    context = { "products" : products }
    return render(request, 'store/store.html', context=context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # https://www.letscodemore.com/blog/django-get-or-create/
        order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        print("çalışıyor")
    else:
        items = []
        order = []
        
    context = { "order" : order, "items" : items }
    return render(request, 'store/cart.html', context=context)

def checkout(request):
    context = { }
    return render(request, 'store/checkout.html', context=context)

def view(request, productId):
    product = models.Product.objects.get(id=productId)
    productImages = list(product.getImageList)
    activeImage = None
    for product in productImages:
        if product.image_order == 1:
            activeImage = product
            productImages.remove(product)
    iterator = range(2, len(productImages))
    product = models.Product.objects.get(id=productId)
    context = { "product" : product, "productImages" : productImages, "activeImage" : activeImage, "iterator" : range(1, len(productImages) + 1) }
    return render(request, 'store/view.html', context=context)