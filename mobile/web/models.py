from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length=100)
    price =models.IntegerField()
    image =models.ImageField(upload_to='media/product_image')

    def __str__(self):
        return self.name
    



class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=40)
    Lastname=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Address=models.TextField()
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pincode=models.IntegerField()
    Phone=models.IntegerField()
    Email=models.EmailField(max_length=50)

    def __str__(self):
        return self.Firstname
    
class OrderItem(models.Model):
     order=models.ForeignKey(Order,on_delete=models.CASCADE)
     product=models.CharField(max_length=50)
     image=models.ImageField(upload_to='media/order_image')
     quantity=models.IntegerField()
     price=models.IntegerField()
     total=models.IntegerField()
     paid=models.BooleanField(default=False)

     def __str__(self):
         return self.product
     

class from_date(models.Model):
    
    Email=models.EmailField()



class contact_date(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=100)



class Leave(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    website=models.CharField(max_length=100)
    comment=models.CharField(max_length=100)



    