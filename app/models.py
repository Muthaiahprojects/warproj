from django.db import models

# Create your models here.
class card(models.Model):
    category = models.CharField(max_length=200)
    img =models.ImageField(upload_to='media')
    model = models.CharField(max_length=200,null='True')
    brand = models.CharField(max_length=200, null='True')
    info = models.CharField(max_length=200, null='True')
    price = models.PositiveIntegerField()

#product details
class product_details(models.Model):

    model = models.CharField(max_length=200)
    details = models.TextField(max_length=200)
    specs = models.TextField()

#cart model
class cart_model(models.Model):
    category = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media')
    model = models.CharField(max_length=200,null='True')
    brand = models.CharField(max_length=200, null='True')
    info = models.CharField(max_length=200, null='True')
    price = models.PositiveIntegerField()
