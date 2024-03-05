from django.shortcuts import render
from . import models
from django.http import JsonResponse
import json

# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = { 'summary_item_count':0, 'summary_item_price':0 }
    products = models.Product.objects.all()
    context = { "products" : products, "order":order }
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
        order = { 'summary_item_count':0, 'summary_item_price':0 }
        
    context = { "order" : order, "items" : items }
    return render(request, 'store/cart.html', context=context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = { 'summary_item_count':0, 'summary_item_price':0 }
    
    context = { "order" : order }
    return render(request, 'store/checkout.html', context=context)

def view(request, productId):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = { 'summary_item_count':0, 'summary_item_price':0 }
        
    
    product = models.Product.objects.get(id=productId)
    productImages = list(product.getImageList)
    activeImage = None
    for product in productImages:
        if product.image_order == 1:
            activeImage = product
            productImages.remove(product)
    iterator = range(2, len(productImages))
    product = models.Product.objects.get(id=productId)
    context = { "order" : order, "product" : product, "productImages" : productImages, "activeImage" : activeImage, "iterator" : range(1, len(productImages) + 1) }
    return render(request, 'store/view.html', context=context)

def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action: ', action)
    print('Product Id: ', productId)
    
    customer = request.user.customer
    product = models.Product.objects.get(id=productId)
    order, created = models.Order.objects.get_or_create(customer=customer, complete='False')
    orderItem, created = models.OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == "add":
        orderItem.amount = orderItem.amount + 1
    elif action == "remove":
        orderItem.amount = orderItem.amount - 1
        
    orderItem.save()
    
    if orderItem.amount <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was updated!', safe=False)
        