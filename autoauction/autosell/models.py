from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
<<<<<<< HEAD
    username = models.CharField(max_length=150, unique=True)
=======
>>>>>>> e0bf5188d887d3d0c3a7fef246dafd8da9b23d35
    STATUS_CHOICES = (
    ('seller', 'Seller'),
    ('buyer', 'Buyer')
    )
    phone_number = PhoneNumberField()

class Car(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('cvt', 'Cvt'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, help_text="Система Передачи")
    mileage = models.PositiveIntegerField(help_text="Пробег в километрах")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Auction(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('finished', 'Finished'),
        ('canceled', 'Canceled'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='auctions')
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')


class Bid(models.Model):
    auction = models.ForeignKey('Auction', on_delete=models.CASCADE, related_name='bids')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_feedbacks')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='given_feedbacks')
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('seller', 'buyer')

    def __str__(self):
        return f"{self.buyer.username} → {self.seller.username}: {self.rating}★"