from django.conf import settings
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


#creat customer profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=25, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zone = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    old_cart = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

#create a profile for a user by default when registerd
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile (user=instance)
        user_profile.save()

#automate the profile
post_save.connect(create_profile, sender=User)





class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'

class Line(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Lines'

    def __str__(self):
        return self.name


class Product (models.Model):
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    line = models.ForeignKey(Line, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.FloatField(null=True, blank=True)




    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quatity = models.IntegerField(default=1)
    address =models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank = True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product