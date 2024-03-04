from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class ProductDetail(models.Model):
    description = models.CharField(max_length=500)
    
    # Teknik Özellikler
    batteryType = models.CharField(max_length=50)
    batteryCellCount = models.CharField(max_length=50)
    security = models.CharField(max_length=50)
    
    # Ram Özellikleri
    ram = models.CharField(max_length=50)
    ramType = models.CharField(max_length=50)
    
    # Ekran Kartı
    graphicsCardChipsetBrand = models.CharField(max_length=50)
    graphicsCardChipset = models.CharField(max_length=50)
    graphicsCardMemoryType = models.CharField(max_length=50)
    graphicsCardMemory = models.CharField(max_length=50)
    graphicsCardType = models.CharField(max_length=50)
    
    # HDD Özellikleri
    diskCapacity = models.CharField(max_length=50)
    diskType = models.CharField(max_length=50)
    
    # Power
    power = models.CharField(max_length=50)
    
    # Multimedia
    multimediaHeadphoneOutput = models.CharField(max_length=50)
    multimediaFeatures = models.CharField(max_length=50)
    multimediaCamera = models.CharField(max_length=50)
    multimediaFingerprintReader = models.CharField(max_length=50)
    
    # Keyboard
    keyboard = models.CharField(max_length=50)
    
    # Monitor
    monitor = models.CharField(max_length=50)
    
    # İşletim Sistemi
    operatingSystem = models.CharField(max_length=50)
    
    # Genel Özellikler
    color = models.CharField(max_length=50)
    fastCharging = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    guarantee = models.CharField(max_length=50)
    
    # İşlemci Tipi
    processorType = models.CharField(max_length=50)
    processorGen = models.CharField(max_length=50)
    processorTech = models.CharField(max_length=50)
    processorNum = models.CharField(max_length=50)
    processorSpeed = models.CharField(max_length=50)
    processorCache = models.CharField(max_length=50)
    processorCore = models.CharField(max_length=50)
    
    # Ekran Özellikleri
    screenSize = models.CharField(max_length=50)
    screenrRefreshRate = models.CharField(max_length=50)
    screenFeatures = models.CharField(max_length=50)
    screenResolution = models.CharField(max_length=50)
    screenIPS = models.CharField(max_length=50)
    screenFullHD = models.CharField(max_length=50)
    screenHD = models.CharField(max_length=50)
    screenTN = models.CharField(max_length=50)
    screenTouch = models.CharField(max_length=50)
    
    # Bağlantı Özellikleri + Portlar
    connectionSpecificationUSB20 = models.CharField(max_length=50)
    connectionSpecificationUSB32 = models.CharField(max_length=50)
    connectionSpecificationUSBTypeC = models.CharField(max_length=50)
    connectionSpecificationBluetoothTech = models.CharField(max_length=50)
    connectionSpecificationEtherner = models.CharField(max_length=50)
    connectionSpecificationWiFi = models.CharField(max_length=50)
    connectionSpecificationHDMI = models.CharField(max_length=50)
    connectionSpecificationCardSlot = models.CharField(max_length=50)
    connectionSpecificationBluetooth = models.CharField(max_length=50)
    
    # Diğer
    illuminatedKeyboard = models.CharField(max_length=50)
    intendedUse1 = models.CharField(max_length=50)
    intendedUse2 = models.CharField(max_length=50)
    manufacturerPartNumber = models.CharField(max_length=50)
    
    # Ağırlık & boyutlar
    weight = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    width = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.id)
    
       
class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.FloatField()
    productDetail = models.ForeignKey(ProductDetail, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"{self.brand} {self.name}"
    
    @property
    def getImage(self):
        try:
            image_url = self.itemimage_set.filter(product=self, image_order=1).get().image.url
        except:
            image_url = ''
        return image_url

class ItemImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    image_order = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)

# Order ile OrderItem mantığına internetten baktım
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=500)
    address_optional = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.id)