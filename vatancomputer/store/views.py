from django.shortcuts import render
from . import models
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
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
        items = order.orderitem_set.all()
    else:
        items = []
        order = { 'summary_item_count':0, 'summary_item_price':0 }
    
    if (request.method == "POST") and (request.POST is not None):
        clean_data = request.POST
        print("add 1")
        if (request.user.is_authenticated == False):
            firstName = clean_data['firstName']
            lastName = clean_data['lastName']
            username = clean_data['username']
            email = clean_data['email']
        else:
            print("add 2")
            address1 = clean_data['address']
            address2 = clean_data['address2']
            city = clean_data['city']
            zipcode = clean_data['zipcode']
            payment_method = clean_data['paymentMethod']
            cartName = clean_data['cartName']
            cartNumber = clean_data['cartNumber']
            cartExpiration = clean_data['cartExpiration']
            cartCvv = clean_data['cartCvv']

            paymentInformation = models.PaymentInformation(customer=customer, payment_method=payment_method, card_name=cartName
                                                                        ,card_number=cartNumber, expires_end=cartExpiration, cvv=cartCvv)
            paymentInformation.save()
            shippingAdress = models.ShippingAddress.objects.create(customer=customer, payment_info=paymentInformation, 
                                                order=order, address=address1, address_optional=address2, 
                                                city=city, zipcode=zipcode)
            shippingAdress.save()
            return redirect(reverse('store:store'))

            
    product = models.Product.objects.all()
    context = { "order" : order, "items" : items }
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

def complete_order(request):
    data = json.loads(request.body)
    orderId = data['orderId']
    action = data['action']
    
    customer = request.user.customer
    order, created = models.Order.objects.get_or_create(customer=customer, complete='False')
    orderItems = order.orderitem_set.all()
    
    if action == "complete" and len(orderItems) > 0:
        for item in orderItems:
            item.product.amount = item.product.amount - item.amount
            item.product.save()
        order.complete = True
    
    order.save()
        
    return JsonResponse('Payment is successful!', safe=False)