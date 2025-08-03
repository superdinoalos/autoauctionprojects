from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator


class UserProfile(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(18), MaxValueValidator(65)
    ], null=True, blank=True)
    STATUS_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    )
    status= models.CharField(max_length=32, choices=STATUS_CHOICES, default='buyer')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Brand(models.Model):
    brand_name = models.CharField(max_length=32)

    def __str__(self):
        return self.brand_name


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.brand}, {self.model_name}'


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=24)
    mileage = models.PositiveIntegerField()
    transmission = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sellers')

    def __str__(self):
        return f"{self.brand.brand_name} {self.model.model_name} ({self.year})"


class CarImages(models.Model):
    cars = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_image')
    car_image = models.ImageField(upload_to='car_img/')

    def __str__(self):
        return f'{self.cars}'


class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_auctions')
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('finished', 'Finished'),
        ('canceled','Canceled' )
    )
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return f'{self.car}, {self.status}'


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount}'


class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='seller_car')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='buyer_cars')
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    comment = models.TextField()
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer}, {self.seller}'



